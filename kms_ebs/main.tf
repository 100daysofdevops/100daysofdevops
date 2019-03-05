provider "aws" {
  region = "us-west-2"
}

resource "aws_ebs_volume" "my-test-kms-ebs" {
  availability_zone = "us-west-2a"
  size              = 10
  type              = "gp2"
  encrypted         = true
  kms_key_id        = "${var.kms_key}"
}
