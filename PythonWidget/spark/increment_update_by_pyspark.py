# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date  : 2020/5/18
"""
使用pyspark进行数据库增量更新，可用于ETL作业
"""

from typing import Union, List, TypeVar

from enum import Enum

from pyspark.sql import functions as F
from pyspark.sql import types
from pyspark.sql import DataFrame
from pyspark.sql.session import SparkSession


class IncrementUpdateByPyspark:
    spark: SparkSession = None
    properties: dict = None
    url: str = None
    table: str = None

    @staticmethod
    def read_table(spark: SparkSession, table: str, properties: dict = None, url: str = None) -> DataFrame:
        if url is None:
            url = properties.get("url", None)
        assert url is not None, "you should support jdbc url."
        return spark.read.jdbc(url, table, properties=properties)

    @staticmethod
    def union(pre_dataframe: DataFrame, post_dataframe: DataFrame) -> DataFrame:
        return pre_dataframe.unionAll(post_dataframe)

    @staticmethod
    def take_by_key(dataframe: DataFrame,
                    key: Union[str, list],
                    include: list = None,
                    exclude: list = None,
                    ascending: Union[bool, List[Union[int, bool]]] = False) -> DataFrame:

        dataframe = dataframe.sort(key, ascending=ascending)
        if include is not None:
            dataframe = dataframe.dropDuplicates(subset=include)
        elif exclude is not None:
            subset = set(dataframe.columns) - set(exclude)
            subset = list(subset)
            dataframe = dataframe.dropDuplicates(subset=subset)
        return dataframe

    @staticmethod
    def update_by_key(pre_dataframe: DataFrame,
                      post_dataframe: DataFrame,
                      key: str,
                      include: list = None,
                      exclude: list = None,
                      ascending: bool = False,
                      update_only: bool = True,
                      ) -> DataFrame:
        r = (
            IncrementUpdateByPyspark.take_by_key(
                IncrementUpdateByPyspark.union(pre_dataframe, post_dataframe),
                key, include, exclude, ascending
                                     )
                )
        if update_only:
            r = r.subtract(pre_dataframe)
        return r


if __name__ == '__main__':

    """readme
    >>> properties = {...}
    >>> url = "..."
    >>> table = "..."
    >>> spark = SparkSession.builder..getOrCreate()
    >>> pre_dataframe = IncrementUpdateByPyspark.read_table(spark, table, properties, url)
    >>> post_dataframe = <your-new-yield-pyspark-dataframe>
    # 需要有主键（或联合主键），需要指定排序键（比如时间，升序或降序）
    >>> dataframe_to_update = IncrementUpdateByPyspark.update_by_key(
                                    pre_dataframe,
                                    post_dataframe,
                                    key: <排序键>,
                                    include: <主键或联合主键>,
                                    exclude: <除指定外全部作为联合主键>, --> 注意，只需要设定include或者exclude其一即可
                                    ascending: <排序键是按递增还是递减>,
            )
    # 清空中间表            
    # 写入中间表
    >>> dataframe_to_update.write.jdbc(..., mode="append")
    # 根据中间表主键删除主表数据
    # 将中间表数据append到主表
    """

    spark = SparkSession.builder.appName("test increament update").getOrCreate()
    schema = types.StructType(
        [
            types.StructField("id", types.IntegerType()),
            types.StructField("num2", types.IntegerType()),
            types.StructField("num3", types.IntegerType()),
            types.StructField("date", types.StringType()),
        ]
    )
    d = [
        [1, 2, 3, "2020-01-01"],
        [2, 2, 5, "2020-10-01"],
        [3, 2, 7, "2019-01-01"],
    ]
    d2 = [
        [1, 2, 5, "2020-02-01"],
        [2, 2, 7, "2020-12-01"],
        [3, 2, 7, "2018-01-01"],
    ]
    dataframe1 = spark.createDataFrame(d, schema=schema)
    dataframe2 = spark.createDataFrame(d2, schema=schema)
    IncrementUpdateByPyspark.update_by_key(dataframe1, dataframe2,
                                           "date",
                                           include=["id"],
                                           ascending=True,
                                           ).show()
