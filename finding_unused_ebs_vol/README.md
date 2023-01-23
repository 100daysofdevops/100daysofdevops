# Python script to find unused EBS Volume

Python script to find unused EBS volume.

## Usage

```python3 finding_unused_ebs_volume.py -h
usage: finding_unused_ebs_volume.py [-h] [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File name to write the list of unused volumes
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

