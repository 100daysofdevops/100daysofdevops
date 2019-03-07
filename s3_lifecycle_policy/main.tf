provider "aws" {
  region = "us-west-2"
}
resource "aws_s3_bucket" "bucket" {
  bucket = "terraform-20181219040316452900000001"
  acl = "private"
  lifecycle_rule {
    enabled = true
    transition {
      days = 30
      storage_class = "STANDARD_IA"
    }
    transition {
      days = 60
      storage_class = "GLACIER"
    }
  }
}