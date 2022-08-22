# Databricks notebook source
# MAGIC %md
# MAGIC #Notebook 1

# COMMAND ----------

default_name = "unknown"

# use notebook param
dbutils.widgets.text("name", default_name, "Enter user name")
user_name = dbutils.widgets.get("name")

if user_name == "unknown":
    greeting = "ERROR"
else:
    greeting = f"Hello {user_name}"

dbutils.notebook.exit(greeting)
