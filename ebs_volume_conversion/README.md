# Python script to convert EBS Volume

Python script to convert EBS volume from gp2 to gp3 or from io1 to io2 and read input from csv file with a format volume_id,volume_type

## Usage

```python3 ebs_volume_conversion.py -h
usage: ebs_volume_conversion.py [-h] [-f FILE] volume_id volume_type

positional arguments:
  volume_id             The EBS volume id of the Volume to be convert
  volume_type           The new EBS volume type to be converted gp3 or io2

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  A csv file containing ebs volume id and volume type to convert
```

# Example

1. To convert an ebs volume from gp2 to gp3

```
python3 ebs_volume_conversion.py -volume_id <vol-id> -volume_type gp3
```

2. To convert an ebs volume from io1 to io2
```
python3 ebs_volume_conversion.py -volume_id <vol-id> -volume_type io2
```

3. You can pass a csv file containing ebs volume id and volume type to convert
```
python3 ebs_volume_conversion.py -f ebs_volume.csv
```
