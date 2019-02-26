provider "aws" {
  region = "us-west-2"
}
resource "aws_s3_bucket_policy" "s3policy" {
  bucket = "mytests3bucket"

  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Id": "MYBUCKETPOLICY",
  "Statement": [
    {
      "Sid": "IPAllow",
      "Effect": "Allow",
      "Principal": "*",
       "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::mytests3bucket*",
      "Condition": {
         "IpAddress": {"aws:SourceIp": "192.168.0.2/24"}
      }
    }
  ]
}
POLICY
}
