provider "aws" {
  region = "us-west-2"
}

resource "aws_iam_role" "my-config" {
  name = "config-example"

  assume_role_policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "config.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
POLICY
}

resource "aws_iam_role_policy_attachment" "my-config" {
  role       = "${aws_iam_role.my-config.name}"
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSConfigRole"
}

resource "aws_s3_bucket" "my-config" {
  bucket = "config-bucket-for-my-test-project"
  acl    = "private"

  versioning {
    enabled = true
  }

  lifecycle {
    prevent_destroy = true
  }
}

resource "aws_config_configuration_recorder" "my-config" {
  name     = "config-example"
  role_arn = "${aws_iam_role.my-config.arn}"

  recording_group {
    all_supported                 = true
    include_global_resource_types = true
  }
}

resource "aws_config_delivery_channel" "my-config" {
  name           = "config-example"
  s3_bucket_name = "${aws_s3_bucket.my-config.bucket}"

  depends_on = ["aws_config_configuration_recorder.my-config"]
}

resource "aws_config_configuration_recorder_status" "config" {
  name       = "${aws_config_configuration_recorder.my-config.name}"
  is_enabled = true

  depends_on = ["aws_config_delivery_channel.my-config"]
}

resource "aws_config_config_rule" "instances_in_vpc" {
  name = "instances_in_vpc"

  source {
    owner             = "AWS"
    source_identifier = "INSTANCES_IN_VPC"
  }

  depends_on = ["aws_config_configuration_recorder.my-config"]
}

resource "aws_config_config_rule" "cloud_trail_enabled" {
  name = "cloud_trail_enabled"

  source {
    owner             = "AWS"
    source_identifier = "CLOUD_TRAIL_ENABLED"
  }

  input_parameters = <<EOF
{
  "s3BucketName": "cloudwatch-to-s3-logs"
}
EOF

  depends_on = ["aws_config_configuration_recorder.my-config"]
}

resource "aws_config_config_rule" "s3_bucket_versioning_enabled" {
  name = "s3_bucket_versioning_enabled"

  source {
    owner             = "AWS"
    source_identifier = "S3_BUCKET_VERSIONING_ENABLED"
  }

  depends_on = ["aws_config_configuration_recorder.my-config"]
}

resource "aws_config_config_rule" "desired_instance_type" {
  name = "desired_instance_type"

  "source" {
    owner             = "AWS"
    source_identifier = "DESIRED_INSTANCE_TYPE"
  }

  input_parameters = <<EOF
{
  "alarmActionRequired" : "t2.micro"
}
EOF

  depends_on = ["aws_config_configuration_recorder.my-config"]
}
