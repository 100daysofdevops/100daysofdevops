import boto3
import argparse

def find_unused_ebs_vol(file_name=None):
    try:
        # Connect to EC2 service
        client = boto3.client('ec2')
        # Finding all the EBS Volumes
        volumes = client.describe_volumes()['Volumes']
        # Initialize a list to store unused EBS volumes
        unused_volumes = []
        # Iterate over the list of unused EBS Volumes
        for vol in volumes:
            # Check if the volume is in unused state
            if vol['State'] == 'available' and not vol['Attachments']:
                print(f'Found unused EBS volume: {vol["VolumeId"]}, Volume Availability Zone: {vol["AvailabilityZone"]}, VolumeType: {vol["VolumeType"]}, Volume Size in GB: {vol["Size"]}')
                unused_volumes.append(vol)

        # Check the condition to see if the filename is provided and store the unused volume in a file

        if file_name is not None:
            with open(file_name,'w') as f:
                for vol in unused_volumes:
                    vol_id = vol["VolumeId"]
                    f.write(str(vol_id) + '\n')
        # Return the list of unused volumes
        return unused_volumes            

    except Exception as e:
        print("An error occurred while trying to get the EBS volumes:", e)
        raise e        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--file',help="File name to write the list of unused volumes")
    args = parser.parse_args()
    find_unused_ebs_vol(args.file) 