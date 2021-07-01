import boto3

ec2 = boto3.resource("ec2")

vol_status={"Name":"status","Values":["available"]}

for vol in ec2.volumes.filter(Filters=[vol_status]):
    vol_id = vol.id
    volume = ec2.Volume(vol.id)
    print("Cleanup EBS volume: ", vol_id)
    volume.delete()
