# Databricks notebook source
dbutils.fs.rm("/FileStore/tables", True)

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, col, explode
import pyspark.sql.functions as f

# COMMAND ----------

spark = SparkSession.builder.appName("ETL Pipeline").getOrCreate()
df = spark.read.text("/FileStore/tables/WordData.txt")

# COMMAND ----------

print(df)

# COMMAND ----------

print(type(df))

# COMMAND ----------

df.show()

# COMMAND ----------

df2 = df.withColumn("splitedData",f.split("value"," "))

# COMMAND ----------

print(df2)

# COMMAND ----------

df2.show()

# COMMAND ----------

df3 = df2.withColumn("words",explode("splitedData"))

# COMMAND ----------

df3.show()

# COMMAND ----------

wordsDF = df3.select("words")

# COMMAND ----------

wordsDF.show()

# COMMAND ----------

wordCount = wordsDF.groupBy("words").count()

# COMMAND ----------

wordCount.show()

# COMMAND ----------

wordCount.count()

# COMMAND ----------

print(wordCount)

# COMMAND ----------

driver = "com.mysql.cj.jdbc.Driver"
url = "jdbc:mysql://karthick1808.c0yl1qlc1wgt.ap-south-1.rds.amazonaws.com/"
table = "karthick.demo123"
user = "karthick1808"
password = "Welcome!12345"

wordCount.write.format("jdbc").option("driver", driver).option("url",url).option("dbtable", table).option("mode", "append").option("user",user).option("password", password).save()

# COMMAND ----------


