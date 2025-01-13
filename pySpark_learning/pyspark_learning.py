__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'viv30ek@gmail.com'
__status__ = 'development'

"""
Core classes:

pyspark.SparkContext
Main entry point for Spark functionality.

pyspark.RDD
A Resilient Distributed Dataset (RDD), the basic abstraction in Spark.

pyspark.streaming.StreamingContext
Main entry point for Spark Streaming functionality.

pyspark.streaming.DStream
A Discretized Stream (DStream), the basic abstraction in Spark Streaming.

pyspark.sql.SQLContext
Main entry point for DataFrame and SQL functionality.

pyspark.sql.DataFrame
A distributed collection of data grouped into named columns.


"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create a Spark session
spark = SparkSession.builder.appName("FlattenData").getOrCreate()

# Sample DataFrame creation with nested data
data = [("John@", 25, [{"street": 1, "location": 2}]),
        ("Jane#", 30, [{"street": 3, "location": 4}]),
        ("Mike$", 35, [{"street": 5, "location": 6}])]

columns = ["name", "age", "address"]
df = spark.createDataFrame(data, columns)

# Flatten the nested array column
df_flattened = df.selectExpr("name", "age", "explode(address) as address")\
        .selectExpr("name", "cast(age as STRING) as myage", "address.street", "address.location")

# Extract individual columns from the struct
# df_flattened = df_flattened.selectExpr("name", "age", "address.street", "address.location")

# Show the flattened DataFrame
df_flattened.show()

# Stop the Spark session
spark.stop()
