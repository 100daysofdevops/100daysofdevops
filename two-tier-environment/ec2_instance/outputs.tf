output "ec2_instance" {
  value = "${aws_instance.test_instance.*.id}"
}
