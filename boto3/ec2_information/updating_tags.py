import boto3
import csv

# Export list of EC2 instances to CSV file
ec2 = boto3.resource('ec2')
instances = ec2.instances.all()

with open('ec2-instances.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Instance ID", "Name"])
    for instance in instances:
        writer.writerow([instance.id, instance.tags[0]['Value'] if instance.tags else ""])

# Manually update CSV file with new tag keys and values


# Import updated CSV file and update tags for each EC2 instance
with open('ec2-instances-tags.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip header row
    for row in reader:
        instance_id = row[0]
        tag_key = row[2]
        tag_value = row[3]
        ec2.create_tags(Resources=[instance_id], Tags=[{'Key': tag_key, 'Value': tag_value}])
