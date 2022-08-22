from runtime.nutterfixture import NutterFixture, tag

default_timeout = 600

class TestAllFixture(NutterFixture):
  def __init__(self):
    self.first = ''
    self.second = ''
    self.table_name = "test_table"
    NutterFixture.__init__(self)
    
  def run_first(self):
    self.first = dbutils.notebook.run('./notebook_1', default_timeout, {'name': 'world'})
    
  def assertion_first(self):
    assert(self.first == "Hello world")

  def run_second(self):
    self.second = dbutils.notebook.run('./notebook_2', default_timeout)

  def assertion_name2(self):
    assert(self.code1_result == "error")

  def after_code2(self):
    spark.sql(f"DROP TABLE {self.test_table}")

# COMMAND ----------

result = TestAllFixture().execute_tests()
print(result.to_string())

# Comment out the next line (result.exit(dbutils)) to see the test result report from within the notebook

# push to br2

is_job = dbutils.notebook.entry_point.getDbutils().notebook().getContext().currentRunId().isDefined()
if is_job:
  result.exit(dbutils)