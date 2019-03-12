provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "test-instance" {
  ami = "${var.centos_ami}"
  instance_type = "${var.instance_type}"
  key_name = "${var.key_name}"

  connection {
    user = "centos"
    private_key = "${file(var.key_path)}"
  }

  provisioner "remote-exec" {
    inline = [
    "sudo yum -y install httpd",
    "sudo service httpd start"
    ]
  }
}