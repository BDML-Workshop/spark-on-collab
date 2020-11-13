#Good let test the cration fo a spark session AND context
import findspark
findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("BDML").master("local[*]").getOrCreate()
