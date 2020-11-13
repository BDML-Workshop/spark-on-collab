#Good let test the cration fo a spark session AND context
import findspark
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/default-java"
os.environ["SPARK_HOME"] = "/content/spark-on-collab/spark-3.0.1-bin-hadoop2.7"

findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("BDML").master("local[*]").getOrCreate()
