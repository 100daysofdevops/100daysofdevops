provider "aws" {
  region = "us-west-2"
}

resource "aws_cloudtrail" "my-demo-cloudtrail" {
  name                          = "my-demo-cloudtrail-terraform"
  s3_bucket_name                = "${aws_s3_bucket.s3_bucket_name.id}"
  include_global_service_events = true
  is_multi_region_trail         = true
  enable_log_file_validation    = true
}

resource "aws_s3_bucket" "s3_bucket_name" {
  bucket = "s3-cloudtrail-bucket-with-terraform-code"

  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
{
   "Sid": "AWSCloudTrailAclCheck",
   "Effect": "Allow",
   "Principal": {
      "Service": "cloudtrail.amazonaws.com"
},
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws:s3:::s3-cloudtrail-bucket-with-terraform-code"
},
{
"Sid": "AWSCloudTrailWrite",
"Effect": "Allow",
"Principal": {
  "Service": "cloudtrail.amazonaws.com"
},
"Action": "s3:PutObject",
"Resource": "arn:aws:s3:::s3-cloudtrail-bucket-with-terraform-code/*",
"Condition": {
  "StringEquals": {
     "s3:x-amz-acl": "bucket-owner-full-control"
  }
}
  }
  ]
  }
  POLICY
}
