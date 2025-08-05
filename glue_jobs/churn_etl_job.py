import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job

glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session
job = Job(glueContext)

df = spark.read.csv("s3://telco-churn-data-buckets/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv", header=True)
df = df.dropna()  # Remove nulls

df.write.parquet("s3://telco-churn-data-buckets/processed/", mode="overwrite")
job.commit()

