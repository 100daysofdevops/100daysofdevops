import boto3
import csv

ec2 = boto3.resource('ec2')
instances = ec2.instances.all()

with open('ec2-instances.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Instance ID", "State", "AMI ID", "Platform", "Instance Type", "Public IPv4 Address"])
    for instance in instances:
        writer.writerow([instance.id, instance.state['Name'], instance.image.id, instance.platform, instance.instance_type, instance.public_ip_address])
