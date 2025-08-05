provider "aws" {
  region = "us-east-1"
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

resource "aws_s3_bucket" "telco_data" {
  bucket = "telco-churn-data-hauwa"

  tags = {
    Name = "Telco Churn Data Bucket"
  }
}


# Optional: Attach policy if role already exists
data "aws_iam_role" "existing_glue_role" {
  name = "glue_service_role"
}

resource "aws_iam_role_policy_attachment" "glue_policy" {
  role       = data.aws_iam_role.existing_glue_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
}
