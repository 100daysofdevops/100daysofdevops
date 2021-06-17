import boto3

ec2 = boto3.resource("ec2")

instance_id=input("Please enter the instance id: ")
instance=ec2.Instance(instance_id)
print("Starting EC2 instance")
instance.start()
instance.wait_until_running()
print("Your instance is up and running")
