import boto3
from operator import itemgetter

# Define the maximum number of AMIs to keep
max_count = 5

# Connect to AWS using the default profile
ec2 = boto3.client('ec2')

# Retrieve a list of all AMIs
response = ec2.describe_images(Owners=['self'])

# Sort the list of AMIs by creation date in descending order
sorted_images = sorted(response['Images'], key=itemgetter('CreationDate'), reverse=True)

# Loop through the list of AMIs and delete any that are beyond the max_count threshold
for index, image in enumerate(sorted_images):
    if index >= max_count:
        ec2.deregister_image(ImageId=image['ImageId'])
        print(f"Deregistered AMI {image['ImageId']}")
    else:
        print(f"Keeping AMI {image['ImageId']}")
        break
