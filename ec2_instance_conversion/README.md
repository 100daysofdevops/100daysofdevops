# Python script to convert EC2 instance

Python script to convert EC2 instance from one type to another and read input from csv file with a format instance_id,instance_type


## Usage

```python3 ec2_instance_conversion.py
usage: ec2_instance_conversion.py [-h] [-instance_id INSTANCE_ID]
                                  [-new_instance_type NEW_INSTANCE_TYPE] [-f FILE]

Convert an EC2 instance from one type to another

optional arguments:
  -h, --help            show this help message and exit
  -instance_id INSTANCE_ID
                        The ID of the EC2 instance to convert
  -new_instance_type NEW_INSTANCE_TYPE
                        The new instance type for the EC2 instance
  -f FILE, --file FILE  A CSV file containing a list of instances and new instance types
```

# Example

1. To convert an EC2 instance to t2.medium

```
python3 ec2_instance_conversion.py -instance_id <instance-id> -new_instance_type t2.medium
```


3. You can pass a csv file containing instance id and instance type to convert
```
python3 ec2_instance_conversion.py -f ec2_conversion.csv
```
