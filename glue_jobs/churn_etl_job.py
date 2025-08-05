import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.job import Job

# Setup Spark + Glue context
glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session
job = Job(glueContext)

# ✅ READ from raw S3
df = spark.read.csv("s3://telco-churn-data-hauwa/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv", header=True)

# 🧼 CLEAN the data (remove rows with nulls)
df = df.dropna()

# ✅ WRITE to processed S3 in Parquet format
df.write.parquet("s3://telco-churn-data-hauwa/processed/", mode="overwrite")

# ✅ Mark job complete
job.commit()
