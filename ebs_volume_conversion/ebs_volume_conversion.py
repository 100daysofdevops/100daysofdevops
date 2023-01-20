#!/usr/bin/env python3
# Python script to convert EBS volume from gp2 to gp3 or from io1 to io2 and read input from csv file with a format volume_id,volume_type

import boto3
import argparse
import csv
import sys

def convert_ebs_vol(volume_id,volume_type):
    # Create an EC2 client
    ec2 = boto3.client('ec2')
    # Ask user if he want to take the snapshot before volume conversion
    snapshot = input(f'Do you want to take the snapshot of the following volume {volume_id} before conversion? (y/n)')
    # Take the snapshot if user confirms
    if snapshot.lower() == 'y':
        try:
            snapshot = ec2.create_snapshot(VolumeId=volume_id,Description="Snapshot before converting the EBS volume")
            # Wait for the snapshot to be completed
            waiter = ec2.get_waiter('snapshot_completed')
            waiter.wait(SnapshotIds=[snapshot['SnapshotId']])
            print(f'Sucessfully created the snapshot {snapshot["SnapshotId"]} of volume {volume_id}')
        except Exception as e:
            print(f'An error occurred while creating the snapshot for volume {volume_id}: {e} ')
            exit(1)        
    try:
        # Modify the EBS Volume to the new volume type
        ec2.modify_volume(VolumeId=volume_id, VolumeType=volume_type)
        print(f'Started converting EBS volume {volume_id} to {volume_type}')
        # Wait until the EBS volume is available
        ec2.get_waiter('volume_available').wait(VolumeIds=[volume_id])
        print(f'Sucessfully converted EBS volume {volume_id} to {volume_type}')
    except Exception as e:
        print(f'An error occurred while converting the EBS volume {volume_id}: {e} ')
        exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-volume_id", help="The EBS volume id of the Volume to be convert")
    parser.add_argument("-volume_type", help="The new EBS volume type to be converted gp3 or io2")
    parser.add_argument("-f","--file", help="A csv file containing ebs volume id and volume type to convert")
    args = parser.parse_args()
    if not any(vars(args).values()):
        parser.print_help()
        sys.exit()    

    if args.file:
        with open(args.file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                volume_id = row[0]
                volume_type = row[1]
                convert_ebs_vol(volume_id, volume_type)
    else:
        convert_ebs_vol(args.volume_id, args.volume_type)
