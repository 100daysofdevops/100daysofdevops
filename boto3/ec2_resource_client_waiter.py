import boto3

ec2 = boto3.resource("ec2")
ec2_cli = boto3.client("ec2")

instance_id=input("Please enter the instance id: ")
instance=ec2.Instance(instance_id)
print("Starting EC2 instance")
instance.start()
waiter = ec2_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=[instance_id])
print("Your instance is up and running")
