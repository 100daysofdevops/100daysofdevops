provider "aws" {
  region = "us-west-2"
}

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

data "template_file" "user-init" {
  template = "${file("${path.module}/userdata.tpl")}"
}
