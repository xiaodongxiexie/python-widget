# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date  : 2021/6/25

import logging
import json
from dataclasses import dataclass
from typing import Any, List, Iterator

from elasticsearch import helpers
from elasticsearch import Elasticsearch

logger = logging.getLogger("es.search")

@dataclass
class ElasticSearchBase(object):
    index: str = "idx_search"
    doc_type: str = "search"

    es: Elasticsearch = None


@dataclass
class ElasticSearchMixin(object):

    es: Elasticsearch

    def ping(self):
        return self.es.ping(request_timeout=0.1)

    def info(self):
        return self.es.info()


class ElasticSearchSearch(ElasticSearchBase):
    def search(self, dsl: dict, size: int = 5):
        rets = self.es.search(
            index=self.index, body=dsl, size=size,
            doc_type=self.doc_type,
            filter_path=["hits.hits._source"],
        )

        hits = [obj for obj in rets.get("hits", {}).get("hits", [])]
        hits = [obj["_source"] for obj in hits]
        return hits


class ElasticSearchUpdate(ElasticSearchSearch):

    def insert(self, body, id):

        self.es.index(
            index=self.index,
            doc_type=self.doc_type,
            body=body
        )

    def update_by_query(self, body=None):
        """用于批量更新字段"""
        """
        body = {
            "script": {
                "lang": "painless",
                "inline": "if (ctx._source.status == null){ctx._source.status=3}"
                #"inline": "ctx._source.kw_sourceType= 'trueTime'"   #新增字段kw_sourceType值为trueTime
            }
        }
        """
        self.es.update_by_query(
            index=self.index,
            doc_type=self.doc_type,
            body=body,
        )


class ElastciSearchDelete(ElasticSearchBase):

    def execute_delete(self, query):
        self.es.delete_by_query(
            index=self.index,
            body={"query": query},
            doc_type=self.doc_type,
        )
        return True

    def delete_index(self):
        self.es.indices.delete(self.index)

    def clear(self):
        return self.execute_delete({"match_all": {}})


class ElastciSearchCore(ElasticSearchMixin, ElasticSearchUpdate, ElastciSearchDelete):

    def __init__(self, index: str = None, doc_type: str = None):
        if index is not None:
            self.index = index
        if doc_type is not None:
            self.doc_type = doc_type


class ElasticSearchBodyStructure:

    def __init__(self, doctype: str):
        self.body = {"settings": {}, "mappings": {}}
        self.doctype = doctype

    def set(self, key: str, value: Any, cascades: List[str]):
        first, *others = cascades
        cursor = self.body.setdefault(first, {})
        for level in others:
            cursor = cursor.setdefault(level, {})
        cursor[key] = value
        return self

    def set_number_of_shards(self, number_of_shards: int = 8):
        return self.set("number_of_shards", number_of_shards, ["settings"])

    def set_number_of_replicas(self, number_of_replicas: int = 2):
        return self.set("number_of_replicas", number_of_replicas, ["settings"])

    def set_analysis_synonyms(self, fname: str, aname: str, synonyms: List[str]):
        self.set(
            fname,
            {
                "type": "synonym",
                "synonyms": synonyms,
            },
            ["settings", "analysis", "filter"])
        self.set(
            aname,
            {
                "tokenizer": "standard",
                "filter": [
                    "lowercase",
                    fname,
                ]
            },
            ["settings", "analysis", "analyzer"]
        )
        return self

    def set_field(self, fieldname: str, fieldtype: str, fieldextra: dict = None, auto: bool = True):
        if fieldextra is None:
            fieldextra = {}
        if auto and fieldtype == "text" and "fields" not in fieldextra:
            fieldextra["fields"] = {"keyword": {"type": "keyword", "ignore_above": 256}}
        return self.set(
            fieldname,
            {
                "type": fieldtype,
                **fieldextra
            },
            ["mappings", self.doctype, "properties"]
        )


class Items(ElastciSearchCore):
    similary = [
        "苹果手机,iphone",
        "华为手机,huawei",
    ]
    body = (
        ElasticSearchBodyStructure(ElastciSearchCore.doc_type)
        .set_number_of_replicas(2)
        .set_number_of_shards(8)
        .set_analysis_synonyms("my_synonym_filter", "my_synonyms", similary)
        .set_field("skucode", "keyword")
        .set_field("prodname", "text", fieldextra={"analyzer": "standard", "search_analyzer": "my_synonyms"})
        .set_field("properties", "text")
        .body
    )

    def create(self, objs: Iterator, rebuild: bool = False):
        if self.es.indices.exists(index=self.index):
            if rebuild:
                logger.warning("[rebuild][delete index] %s", self.index)
                self.delete_index()
            else:
                return
        self.es.indices.create(index=self.index, body=self.body)
        logger.info("[create][es][index]%s [doc_type]%s", self.index, self.doc_type)
        actions = []
        for obj in objs:
            actions.append(
                dict(
                    _index=self.index,
                    _type=self.doc_type,
                    _source=obj,
                )
            )
        helpers.bulk(self.es, actions)

    def search(self, dsl: dict, size: int = 5):
        rets = self.es.search(
            index=self.index, body=dsl, size=size,
            doc_type=self.doc_type,
        )

        hits = rets.get("hits", {}).get("hits", [])
        hits = [obj["_source"].update(score=obj["_score"]) or obj["_source"] for obj in hits]
        return hits

    def isearch(self, prodname: str, properties: str, skucode: str = "", size: int = 5):
        """
        相似商品搜索
        :param prodname:     商品名称
        :param properties:   商品属性
        :param skucode:      用于过滤自身
        :param size:         返回商品个数
        :return:
        """
        dsl = {
            "query": {
                "bool": {
                    "must": [{"match": {"properties": properties}}],
                    "should": [
                        {"match": {"prodname": {"query": prodname, "boost": 2.0}}},
                        # {"match": {"properties": properties}}
                    ],
                    "filter": {
                        "bool": {
                            "must_not": [{"term": {"skucode": skucode}}]  # 过滤掉自身
                        }
                    },
                },
            }
        }

        logger.debug("[elasticsearch][dsl] %s", json.dumps(dsl, indent=4, ensure_ascii=False))

        return self.search(dsl, size=size)


    def dslsearch(self, prodname: str, properties: str, skucode: str = "", size: int = 5):
        """
        理论上效果应该跟 isearch 一致，只是采用 ORM 样式查询
         :param prodname:     商品名称
        :param properties:   商品属性
        :param skucode:      用于过滤自身
        :param size:         返回商品个数
        :return:
        """

        from elasticsearch_dsl import Search

        s = (
            Search(using=self.es, index=self.index, doc_type=self.doc_type)
            .query("match", prodname=prodname)
            .query("match", properties=properties)
            .exclude("term", skucode=skucode)
            .extra(size=size)
        )

        logger.debug("[elasticsearch][dsl] %s", json.dumps(s.to_dict(), indent=4, ensure_ascii=False))
        s = s.execute()
        return s
