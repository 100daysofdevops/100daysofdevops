provider "aws" {
  region = "us-west-2"
}
module "s3_endpoint" {
  source = "./s3_endpoint"
  vpc_id = "vpc-01e4320a539fc7c9b"
  route_table ="rtb-019e305806e020507"
}

module "logs_endpoint" {
  source = "./logs_endpoint"
  vpc_id = "vpc-01e4320a539fc7c9b"
  subnet_id = "subnet-0a9bab91cafe6bc2e"
  security_group = "sg-059f0331c447cd268"
}