import boto3

ec2 = boto3.resource("ec2")

ec2_instance = {"Name": "instance-type", "Values": ["t2.micro"]}

for instance in ec2.instances.filter(Filters=[ec2_instance]):
    instance.stop()
