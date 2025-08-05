import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.job import Job

# Setup
glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session
job = Job(glueContext)

# Read CSV
input_path = "s3://telco-churn-data-hauwa/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv"
print(f"Reading from: {input_path}")
df = spark.read.csv(input_path, header=True)

# Drop nulls and count
df = df.dropna()
print(f"Row count after cleaning: {df.count()}")

# Write to Parquet
output_path = "s3://telco-churn-data-hauwa/processed/"
print(f"Writing to: {output_path}")
df.write.parquet(output_path, mode="overwrite")

job.commit()
