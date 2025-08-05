provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "telco_data" {
  bucket = "telco-churn-data-buckets"
}

resource "aws_iam_role" "glue_service_role" {
  name = "glue_service_role"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Action": "sts:AssumeRole",
    "Principal": {
      "Service": "glue.amazonaws.com"
    },
    "Effect": "Allow",
    "Sid": ""
  }]
}
EOF
}

resource "aws_iam_role_policy_attachment" "glue_policy" {
  role       = aws_iam_role.glue_service_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
}

# Glue Job setup will be dynamic – we'll reference this role

