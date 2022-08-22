# Databricks notebook source
# MAGIC %md
# MAGIC # Notebook 2

# COMMAND ----------

from pyspark.sql import SparkSession


def generate_data(table_name="test_table"):
  df = SparkSession.getActiveSession().range(0,10)
  df.write.format("delta").mode("overwrite").saveAsTable(table_name)

generate_data()
