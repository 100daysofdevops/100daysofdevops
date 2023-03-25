import boto3
from datetime import datetime
from dateutil.parser import parse

# Set the tag key and value to use for filtering AMIs
tag_key = "my-tag-key"
tag_value = "my-tag-value"

# Set the maximum number of days to keep an AMI
max_age_days = 2

# Set the list of regions to clean up AMIs
regions = ["us-west-1", "us-west-2", "us-east-1"]

# Loop through each region and clean up AMIs
for region in regions:
    # Connect to EC2 in the current region using the default profile
    client = boto3.client("ec2", region_name=region)

    # Get a list of all the AMIs with the specified tag
    my_ami = client.describe_images(
        Owners=["self"],
        Filters=[
            {
                "Name": f"tag:{tag_key}",
                "Values": [tag_value]
            }
        ]
    )["Images"]

    # Loop through the list of AMIs and delete any that are older than the maximum age
    for ami in my_ami:
        creation_date = parse(ami["CreationDate"]).replace(tzinfo=None)
        ami_id = ami["ImageId"]
        age_in_days = (datetime.now() - creation_date).days
        print(f"Checking AMI {ami_id} in region {region} with age {age_in_days} days")
        if age_in_days > max_age_days:
            client.deregister_image(ImageId=ami_id)
            print(f"Deleted AMI {ami_id} in region {region} with age {age_in_days} days")
