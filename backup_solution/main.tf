provider "aws" {
  region = "us-west-2"
}

module "ec2_instance" {
  source        = "./ec2_instance_s3_role"
  test_ami      = "ami-01ed306a12b7d1c96"
  instance_type = "t2.micro"
}

module "vpc_endpoint" {
  source      = "./vpc_endpoint"
  vpc_id      = "vpc-03e162e6b83d51d68"
  route_table = "rtb-0af53c788e56135ea"
}

module "s3_bucket_policy" {
  source = "./s3_bucket_policy"
}
