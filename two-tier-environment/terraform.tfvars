vpc_cidr = "10.0.0.0/16"
public_cidrs
 = [
"10.0.1.0/24",
"10.0.2.0/24"
]
private_cidrs
= [
        "10.0.3.0/24",
        "10.0.4.0/24"
]


instance_count = 2
instance_type = "t2.micro"
my_public_key = "/tmp/id_rsa.pub"

alarm_actions = "laprashant@gmail.com"

