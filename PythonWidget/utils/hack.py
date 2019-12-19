from pyspark.sql import SparkSession
from pyspark import SparkConf


spark = SparkSession.builder.config(conf=SparkConf()).getOrCreate()
sc = spark.sparkContext


rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 2),("a",8),("c",4), ("a", 12),("a",18),("c",14)],2)


# hack 
# 使用append,extend 返回值
rdd.combineByKey(lambda obj: [obj], lambda obj1, obj2: obj1 if not obj1.append(obj2) else 0, 
                                     lambda obj1, obj2: obj1 if not obj1.extend(obj2) else 0).collect()
