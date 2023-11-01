import re
from pyspark import SparkConf  # Spark Configuration
from pyspark import SparkContext  # Spark Context

conf = SparkConf().setMaster("local[*]")
spark = SparkContext(conf=conf)

rdd_init = spark.textFile(
    "/home/nukeexplode/Desktop/tkqtools/test.txt")
# print(type(rdd_init))
rdd_flatmap = rdd_init.flatMap(
    lambda line: re.split(r'\t', line))  # Return PipelinedRDD
  # flatmap, 对元素内部继续进行 map，深层次的 map  
# 查看数据
print(rdd_flatmap.collect())
