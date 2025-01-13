import unittest
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from my_spark_script import process_data
from my_spark_script import perform_join


class TestMySparkScript(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a Spark session for the entire test class
        cls.spark = SparkSession.builder.appName("UnitTest").getOrCreate()

    @classmethod
    def tearDownClass(cls):
        # Stop the Spark session after all tests in the class
        cls.spark.stop()

    def test_perform_join(self):
        # Sample data for testing
        data1 = [(1, "John"), (2, "Jane"), (3, "Mike")]
        columns1 = ["id", "name"]
        df1 = self.spark.createDataFrame(data1, columns1)

        data2 = [(1, "Engineer"), (2, "Doctor"), (3, "Teacher")]
        columns2 = ["id", "occupation"]
        df2 = self.spark.createDataFrame(data2, columns2)

        # Call the function to perform the join
        result_df = perform_join(df1, df2)

        # Define the expected result
        expected_data = [(1, "John", "Engineer"), (2, "Jane", "Doctor"), (3, "Mike", "Teacher")]
        expected_columns = ["id", "name", "occupation"]
        expected_df = self.spark.createDataFrame(expected_data, expected_columns)

        # Assert that the actual result matches the expected result
        self.assertTrue(result_df.collect() == expected_df.collect())

    def test_process_data(self):
        # Sample data for testing
        data = [("value_A", "value_B", "value_C", "distinct_value"),
                ("value_D", "value_E", "value_F", "distinct_value"),
                ("value_G", "value_H", "value_I", "another_distinct_value")]
        columns = ["col_A", "col_B", "col_C", "col_D"]
        df_input = self.spark.createDataFrame(data, columns)

        # Distinct values to use in the filter
        distinct_values = ["distinct_value"]

        # Call the function to process the data
        result_df = process_data(df_input, distinct_values)

        # Define the expected result
        expected_data = [("value_A", "value_B", "value_C", "distinct_value", current_timestamp()),
                         ("value_D", "value_E", "value_F", "distinct_value", current_timestamp())]
        expected_columns = ["col_a", "col_B", "col_C", "col_D", "insertDate"]
        expected_df = self.spark.createDataFrame(expected_data, expected_columns)

        # Assert that the actual result matches the expected result
        self.assertTrue(result_df.collect() == expected_df.collect())

      