import boto3

ec2 = boto3.client("ec2")

instance_id=input("Please enter the instance id: ")
print("Starting EC2 instance")
instance=ec2.start_instances(InstanceIds=[instance_id])
waiter = ec2.get_waiter('instance_running')
waiter.wait(InstanceIds=[instance_id])
print("Your instance is up and running"
