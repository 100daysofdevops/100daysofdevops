import boto3

ec2 = boto3.resource("ec2")

for vol in ec2.volumes.all():
    vol_id = vol.id
    volume = ec2.Volume(vol.id)
    desc = 'This is a snapshot of {}'.format(vol_id)
    print("Creating Snapshot of the following Volume : ", vol_id)
    volume.create_snapshot(Description=desc)
