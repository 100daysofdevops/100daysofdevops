import boto3
from datetime import datetime, timedelta, timezone

ec2 = boto3.resource('ec2')

current_date = datetime.now(tz=timezone.utc)
diff_date = current_date - timedelta(days=10)


snapshots = ec2.snapshots.filter(OwnerIds=['self'])
for snapshot in snapshots:
    snapshot_start_time = snapshot.start_time
    if diff_date > snapshot_start_time:
        try:
            snapshot.delete()
            print("Deleting Snapshot id: ", snapshot.snapshot_id)
            
        except Exception as e:
            print("Current Snapshot is in use: ", snapshot.snapshot_id)
            continue
