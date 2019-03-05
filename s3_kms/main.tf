provider "aws" {
  region = "us-west-2"
}
resource "aws_s3_bucket" "mybucket" {
  bucket = "mys3bucket-withkms-serverside-encryption"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        kms_master_key_id = "${var.kms_key}"
        sse_algorithm     = "aws:kms"
      }
    }
  }
}