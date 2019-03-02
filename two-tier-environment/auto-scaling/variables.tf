variable "image_id" {
  default = "ami-095cd038eef3e5074"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "vpc_id" {
  default = "vpc-8d8f76f4"
}

variable "target_group_arn" {
  default = "arn:aws:elasticloadbalancing:us-west-2:349934551430:targetgroup/my-alb-tg/85a23209f9c37964"
}
