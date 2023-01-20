#!/usr/bin/env python3
# Python script to convert EC2 instance from one type to another and read input from csv file with a format instance_id,instance_type

import argparse
import boto3
import sys
import csv

def convert_instance(instance_id, new_instance_type, csv_file=None):
    # Create an EC2 client
    ec2 = boto3.client('ec2')
    
    # Check if the instance is in a stopped state
    response = ec2.describe_instances(InstanceIds=[instance_id])
    instance_state = response['Reservations'][0]['Instances'][0]['State']['Name']
    if instance_state == 'stopped':
        snapshot_response = input("The instance is in a stopped state. Please don't forget to take the ebs snapshot of the instance volume before the conversion y/n")
    try:
        # Modify the instance
        ec2.modify_instance_attribute(InstanceId=instance_id, Attribute='instanceType', Value=new_instance_type)
        print("Successfully converted instance", instance_id, "to", new_instance_type)
    except Exception as e:
        print("Error converting instance:", e)

if __name__ == '__main__':
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Convert an EC2 instance from one type to another')
    parser.add_argument('-instance_id', help='The ID of the EC2 instance to convert')
    parser.add_argument('-new_instance_type', help='The new instance type for the EC2 instance')
    parser.add_argument("-f","--file", help='A CSV file containing a list of instances and new instance types')
    args = parser.parse_args()
    if not any(vars(args).values()):
        parser.print_help()
        sys.exit()
    if args.file:
        with open(args.file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                instance_id = row[0]
                new_instance_type = row[1]
                convert_instance(instance_id, new_instance_type)  
    else:
        convert_instance(args.instance_id, args.new_instance_type)            
