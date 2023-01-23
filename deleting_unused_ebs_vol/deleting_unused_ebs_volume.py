import boto3
import argparse
import datetime
import sys

# Create an EC2 client
ec2 = boto3.client('ec2')

def delete_unused_ebs(file_name=None):
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
                snapshot = input(f'Do you want to take a snapshot of volume {volume_id} before deleting? (y/n)')
                if snapshot.lower() == 'y':
                 # Take a EBS snapshot 
                    ec2.create_snapshot(VolumeId=volume_id,Description=f'Snapshot of the volume {volume_id} taken on {datetime.datetime.now()}')
                    print(f'Creating the Snapshot of volume {volume_id}')                   

                print(f'Deleting unused EBS Volume: {volume_id}')
                ec2.delete_volume(VolumeId=volume_id)
            except Exception as e:
                print(f'Error deleting EBS volume {volume_id}: {e}')
    
    # Check the condition to see if the filename is provided and read the ebs volume from the file

    if file_name is not None:
        try:
            with open(file_name, 'r') as f:
                volume_ids = f.read().splitlines()
                for volume_id in volume_ids:
                    snapshot = input(f'Do you want to take a snapshot of volume {volume_id} before deleting? (y/n)')
                    if snapshot.lower() == 'y':
                    # Take a EBS snapshot 
                        ec2.create_snapshot(VolumeId=volume_id,Description=f'Snapshot of the volume {volume_id} taken on {datetime.datetime.now()}')
                        print(f'Creating the Snapshot of volume {volume_id}') 
                    
                    print(f'Deleting unused EBS Volume: {volume_id}')
                    ec2.delete_volume(VolumeId=volume_id)    
        except Exception as e:
            print(f'Error deleting EBS volume {volume_id}: {e}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='Name of the file that contains the list of unused volumes')
    try:
        args = parser.parse_args()
        delete_unused_ebs()
        sys.exit()
    except Exception as e:
        print("An error occurred while parsing the arguments:", e)    
