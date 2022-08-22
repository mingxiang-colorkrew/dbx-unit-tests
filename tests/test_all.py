# Databricks notebook source
from runtime.nutterfixture import NutterFixture, tag

default_timeout = 600


class TestRunningNotebook(NutterFixture):
    def __init__(self):
        self.first = ""
        self.second = ""
        self.table_name = "test_table"
        NutterFixture.__init__(self)

    def run_first(self):
        self.first = dbutils.notebook.run(
            "../notebook_1", default_timeout, {"name": "world"}
        )

    def assertion_first(self):
        assert self.first == "Hello world"

    def run_second(self):
        self.second = dbutils.notebook.run("../notebook_2", default_timeout)
        # function from notebook_2
        generate_data()

    def assertion_second(self):
        test_table = spark.sql(f"SELECT COUNT(*) AS total FROM {self.table_name}")
        first_row = test_table.first()
        assert first_row[0] == 10

    def after_second(self):
        spark.sql(f"DROP TABLE {self.test_table}")


# COMMAND ----------

result = TestAllFixture().execute_tests()
print(result.to_string())

is_job = (
    dbutils.notebook.entry_point.getDbutils()
    .notebook()
    .getContext()
    .currentRunId()
    .isDefined()
)
if is_job:
    result.exit(dbutils)
