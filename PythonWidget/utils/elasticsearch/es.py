# coding: utf-8

import os
import glob
import random

from elasticsearch import Elasticsearch


def read_text(path):
    with open(path, encoding="utf-8") as file:
        return file.read()
        

def read_texts(paths):
    files = []
    for path in paths:
        files.append(read_text(path))
    return files
 

def create_index(es, index): 
    mapping = {
        'properties': {
            'title': {
                'type': 'text',
                #'analyzer': 'ik_max_word',
                #'search_analyzer': 'ik_max_word'
            }
        }
    }
    es.indices.delete(index=index)
    es.indices.create(index=index)
    result = es.indices.put_mapping(index=index, body=mapping, doc_type="politics", include_type_name=True)
    print(result)
    return es
    
    
def main(paths, index="novel"):
    es = Elasticsearch()
    #es = create_index(es, index=index)
    mapping = {
        'properties': {
            'title': {
                'type': 'text',
                #'analyzer': 'ik_max_word',
                #'search_analyzer': 'ik_max_word'
            }
        }
    }
    es.indices.delete(index=index)
    es.indices.create(index=index)
    #result = es.indices.put_mapping(index=index, body=mapping, doc_type="politics", include_type_name=True)
    files = read_texts(paths)
    for file in files:
        file = {
            "title": "novel",
            "text": file,
        }
        es.index(index=index, doc_type="politics", body=file)
        
    return es

    
    
if __name__ == "__main__":

    paths = glob.glob(os.path.join(r"C:\Users\Administrator\Desktop\test\novel\novel\novel_files", "*.txt"))
    index = "novel"
    es = Elasticsearch()
    #es = main(paths, index=index)
    num = es.search(index=index)["hits"]["total"]["value"]
    
    has_seen = set()
    
    dsl = {
            "query": {
                    "match": {
                        "text": "苞米",
                    }
                }
    }
    dsl = {"size": num}
    while True:
        i = random.randint(0, num)
        if i not in has_seen:
            has_seen.add(i)
        else:
            continue
        print(es.search(index=index, body=dsl)["hits"]["hits"][i]["_source"]["text"])
        
        _next = input("继续[y/n]~")
        if not _next.lower().startswith("y"):
            break
    #print(es.search(index=index, body=dsl)["hits"]["hits"][1]["_source"]["text"])
    
    

