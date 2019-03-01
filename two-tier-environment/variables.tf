variable "vpc_cidr" {}

variable "public_cidrs" {
  type = "list"
}

variable "private_cidrs" {
  type = "list"
}

variable "my_public_key" {}
variable "instance_type" {}
variable "instance_count" {}

variable "alarm_actions" {}
