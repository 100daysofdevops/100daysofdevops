>>> import boto3
>>> ec2 = boto3.resource("ec2")
>>> for region in ec2.meta.client.describe_regions()['Regions']:
...     print(region['RegionName'])
