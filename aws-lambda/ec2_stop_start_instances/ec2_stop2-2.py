import boto3

ec2 = boto3.resource("ec2")

ec2_instance = {"Name": "instance-type", "Values": ["t2.micro"]}
ec2_tag = {"Name": "tag:Name", "Values": ["boto3-prod"]}

for instance in ec2.instances.filter(Filters=[ec2_tag]):
    instance.stop()
