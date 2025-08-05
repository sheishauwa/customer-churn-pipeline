provider "aws" {
  region = "us-east-1"
}

# 🪪 Random suffix generator (not used, kept for future safety)
resource "random_id" "bucket_suffix" {
  byte_length = 4
}

# 🪣 Reference existing S3 bucket - No creation to avoid BucketAlreadyExists error
data "aws_s3_bucket" "existing_telco_data" {
  bucket = "telco-churn-data-hauwa"
}

# 👤 Reference existing IAM role - Don't recreate
data "aws_iam_role" "existing_glue_role" {
  name = "glue_service_role"
}

# ✅ Attach Glue policy to existing role
resource "aws_iam_role_policy_attachment" "glue_policy" {
  role       = data.aws_iam_role.existing_glue_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
}
