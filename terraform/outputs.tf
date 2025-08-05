output "bucket_name" {
  value = data.aws_s3_bucket.existing_telco_data.bucket
}
