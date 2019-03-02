output "alb_id" {
  value = "${aws_lb.my-test-lb.name}"
}

output "target_group_arn" {
  value = "${aws_lb_target_group.my-alb-tg.arn}"
}
