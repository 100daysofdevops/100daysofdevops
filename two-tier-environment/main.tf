module "vpc_networking" {
  source        = "./vpc_networking"
  vpc_cidr      = "${var.vpc_cidr}"
  public_cidrs  = "${var.public_cidrs}"
  private_cidrs = "${var.private_cidrs}"
}

module "ec2_instance" {
  source         = "./ec2_instance"
  instance_count = "${var.instance_count}"
  my_public_key  = "${var.my_public_key}"
  instance_type  = "${var.instance_type}"
  subnet_id      = "${module.vpc_networking.public_subnets}"
  security_group = "${module.vpc_networking.security_group}"
}
