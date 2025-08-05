import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job

# Initialize contexts
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load CSV from S3
input_path = "s3://telco-churn-data-hauwa/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv"
df = spark.read.option("header", True).csv(input_path)

# Simple data cleaning: remove rows with nulls
df_clean = df.dropna()

# Save to S3 in Parquet format
output_path = "s3://telco-churn-data-hauwa/processed/"
df_clean.write.mode("overwrite").parquet(output_path)

job.commit()
