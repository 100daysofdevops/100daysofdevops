import boto3
ec2 = boto3.client('ec2')
response = ec2.run_instances(
    ImageId='ami-01ed306a12b7d1c96',
    InstanceType='t2.micro',
    KeyName='vpcflowlogs',
    MinCount=1,
    MaxCount=1
)
print(response)