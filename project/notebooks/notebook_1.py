# Databricks notebook source
# MAGIC %md
# MAGIC #Notebook 1

# COMMAND ----------
from project.core import utilities

default_name = "unknown"

# use notebook param
dbutils.widgets.text("name", default_name, "Enter user name")
user_name = dbutils.widgets.get("name")

if user_name == "unknown":
    greeting = "ERROR"
else:
    greeting = utilities.hello(user_name)

dbutils.notebook.exit(greeting)
