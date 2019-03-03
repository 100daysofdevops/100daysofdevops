provider "aws" {
  region = "us-west-2"
}

resource "aws_launch_configuration" "asg-config" {
  image_id        = "${var.image_id}"
  instance_type   = "${var.instance_type}"
  security_groups = ["${aws_security_group.asg-sg.id}"]

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_security_group" "asg-sg" {
  name   = "my-test-sg"
  vpc_id = "${var.vpc_id}"

  lifecycle {
    create_before_destroy = true
  }
}

# Ingress Security Port 22
resource "aws_security_group_rule" "http_inbound_access" {
  from_port         = 80
  protocol          = "tcp"
  security_group_id = "${aws_security_group.asg-sg.id}"
  to_port           = 80
  type              = "ingress"
  cidr_blocks       = ["0.0.0.0/0"]

  lifecycle {
    create_before_destroy = true
  }
}

# All OutBound Access
resource "aws_security_group_rule" "all_outbound_access" {
  from_port         = 0
  protocol          = "-1"
  security_group_id = "${aws_security_group.asg-sg.id}"
  to_port           = 0
  type              = "egress"
  cidr_blocks       = ["0.0.0.0/0"]

  lifecycle {
    create_before_destroy = true
  }
}

data "aws_availability_zones" "all" {}
resource "aws_autoscaling_group" "test-asg" {
  launch_configuration    = "${aws_launch_configuration.asg-config.id}"
  availability_zones      = ["${data.aws_availability_zones.all.names}"]
  target_group_arns       = ["${var.target_group_arn}"]
  health_check_type       = "ELB"
  min_size                = "1"
  max_size                = "2"
  tag {
    key = "Name"
    propagate_at_launch = true
    value = "my-terraform-asg-example"
  }
}
