import boto3
from datetime import datetime
from dateutil.parser import parse

current_date=datetime.now()

client = boto3.client("ec2")

my_ami = client.describe_images(Owners=['self'])['Images']

for ami in my_ami:
    creation_date=ami['CreationDate']
    creation_date_parse=parse(creation_date).replace(tzinfo=None)
    ami_id = ami['ImageId']
    diff_in_days = (current_date - creation_date_parse).days
    print("Cleaning up all the AMI greater then 2 days old", ami_id)
    if diff_in_days > 2:
        client.deregister_image(ImageId=ami_id)
