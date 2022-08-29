# Databricks notebook source
from runtime.nutterfixture import NutterFixture, tag
from pyspark.sql.types import StructType,StructField, StringType, IntegerType

default_timeout = 600

def create_tables(source_table: str, dest_table: str):
    spark.sql(
        (
            f"CREATE TABLE {source_table} ( "
            f"id INT NOT NULL, "
            f"name STRING "
            f") "
            f"USING DELTA "
        )
    )
    

class TestNotebook4Fixture(NutterFixture):
    def __init__(self):
        self.source_table = "default.notebook_4_source"
        self.dest_table = "default.notebook_4_dest"
        self.mask_result = ""
        NutterFixture.__init__(self)
        
    def before_mask(self):
        create_tables(self.source_table, self.dest_table)

        data = [
            (1, "James"),
            (2, "John"),
            (3, "Jane"),
        ]
        
        schema = StructType([
            StructField("id", IntegerType(), nullable=False),
            StructField("name", StringType(), nullable=False)
        ])
        
        df = spark.createDataFrame(
            data=data,
            schema=schema
        )
        
        (
            df.write
            .format('delta')
            .mode('overwrite')
            .saveAsTable(self.source_table)
        )
        

    def run_mask(self):
        self.mask_result = dbutils.notebook.run(
            "../../notebooks/notebook_4", 
            timeout_seconds=default_timeout, 
            arguments={"source_table": self.source_table, "dest_table": self.dest_table}
        )
    
    def assertion_mask(self):
        dest_table = spark.sql(f"SELECT masked_name AS total FROM {self.dest_table}")
        first_row = dest_table.first()
        assert first_row[0] == "MASKED"

    def after_mask(self):
        spark.sql(f"DROP TABLE {self.source_table}")
        spark.sql(f"DROP TABLE {self.dest_table}")
        
result = TestNotebook4Fixture().execute_tests()
print(result.to_string())

