#!/usr/bin/env python3
# This script is to clean up Amazon Elastic Block Store (EBS) volumes that are in an unused state
# Author: Prashant Lakhera(laprashant@gmail.com)

import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

def delete_unused_ebs():
    # Get the list of all EBS Volumes
    try:
        response = ec2.describe_volumes()
    except Exception as e:
        print(f'Error getting the list of EBS Volumes: {e}')
        return

    # Loop through the list of volumes and check for any unused volumes
    for volume in response['Volumes']:
        if volume['State'] == 'available' and not volume['Attachments']:
            volume_id = volume["VolumeId"]
            try:
                print(f'Deleting unused EBS Volume: {volume_id}')
                ec2.delete_volume(VolumeId=volume_id)
            except Exception as e:
                print(f'Error deleting EBS volume {volume_id}: {e}')

def main():
    delete_unused_ebs()


if __name__ == '__main__':
    main()