output "sns_topic" {
  value = "${aws_sns_topic.alarm.arn}"
}
