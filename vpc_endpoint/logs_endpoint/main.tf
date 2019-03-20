resource "aws_vpc_endpoint" "ec2logs"{
  vpc_id            ="${var.vpc_id}"
  service_name      = "com.amazonaws.us-west-2.logs"
  subnet_ids = ["${var.subnet_id}"]
  vpc_endpoint_type = "Interface"

  security_group_ids = [
    "${var.security_group}"
  ]
  policy = <<POLICY
{
    "Statement": [
        {
            "Action": "*",
            "Effect": "Allow",
            "Resource": "*",
            "Principal": "*"
        }
    ]
}
POLICY
  private_dns_enabled = true
}