provider "aws" {
  region = "us-west-2"
}

data "aws_availability_zones" "available" {}

# To get the latest Centos7 AMI
data "aws_ami" "centos" {
  owners      = ["679593333241"]
  most_recent = true

  filter {
    name   = "name"
    values = ["CentOS Linux 7 x86_64 HVM EBS *"]
  }

  filter {
    name   = "architecture"
    values = ["x86_64"]
  }

  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }
}

resource "aws_key_pair" "mytest-key" {
  key_name   = "my-test-terraform-key"
  public_key = "${file(var.my_public_key)}"
}

resource "aws_instance" "test_instance" {
  count                  = "${var.instance_count}"
  ami                    = "${data.aws_ami.centos.id}"
  instance_type          = "${var.instance_type}"
  key_name               = "${aws_key_pair.mytest-key.id}"
  vpc_security_group_ids = ["${var.security_group}"]
  subnet_id              = "${element(var.subnet_id, count.index )}"
  user_data              = "${data.template_file.user-init.rendered}"

  tags {
    Name = "my-test-server.${count.index + 1}"
  }
}

resource "aws_ebs_volume" "my-test-ebs" {
  count             = 2
  availability_zone = "${data.aws_availability_zones.available.names[count.index]}"
  size              = 10
  type              = "gp2"
}

resource "aws_volume_attachment" "my-test-ebs-attachment" {
  count       = 2
  device_name = "/dev/xvdh"
  instance_id = "${aws_instance.test_instance.*.id[count.index]}"
  volume_id   = "${aws_ebs_volume.my-test-ebs.*.id[count.index]}"
}

data "template_file" "user-init" {
  template = "${file("${path.module}/userdata.tpl")}"
}

resource "aws_cloudwatch_metric_alarm" "cpu-utilization" {
  alarm_name          = "high-cpu-utilization-alarm"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "2"
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = "120"
  statistic           = "Average"
  threshold           = "80"
  alarm_description   = "This metric monitors ec2 cpu utilization"
  alarm_actions       = ["${var.alarm_actions}"]

  dimensions {
    InstanceId = "${aws_instance.test_instance.*.id[count.index]}"
  }
}

resource "aws_cloudwatch_metric_alarm" "instance-health-check" {
  alarm_name          = "instance-health-check"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "1"
  metric_name         = "StatusCheckFailed"
  namespace           = "AWS/EC2"
  period              = "120"
  statistic           = "Average"
  threshold           = "1"
  alarm_description   = "This metric monitors ec2 health status"
  alarm_actions       = ["${var.alarm_actions}"]

  dimensions {
    InstanceId = "${aws_instance.test_instance.*.id[count.index]}"
  }
}
