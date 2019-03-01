variable "my_public_key" {}
variable "instance_type" {}
variable "instance_count" {}
variable "security_group" {}

variable "subnet_id" {
  type = "list"
}

variable "alarm_actions" {}
