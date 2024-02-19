#!/opt/anaconda3/bin/python3

## Modules
import argparse
import pathlib
import datetime

## Function
def search_file_older_than_x_days(path, xdays):
  ## Current Date
  today = datetime.datetime.now()
  if path.is_dir():                                                                   # Checking the given arg is a dir or not
    for item in path.iterdir():                                                       # if it's a dir iterating through each item
      if item.is_file():                                                              # checking if its a file or not
         file_creation_date = datetime.datetime.fromtimestamp(item.stat().st_ctime)   # Fetching the creation time
         days_differ = (today-file_creation_date).days                                # Getting the difference between current date and file creation date
         if days_differ > int(xdays):                                                 # if it's more then specified xdays
           print(item,"older than %x days"%days_differ)                               # if yes print the specified file
  else:
    print("Directory %s doent exists"%path)                                           # Print statement if the given path doesnt exist

## Create the parser
parser = argparse.ArgumentParser()

## Add the arguments
parser.add_argument("--path", help="Directory Path")
parser.add_argument("--days", help="mention days to find files older than x days ")

## Execute the parse_arg() method
args = parser.parse_args()

## Setting up the default values if not passed through cmd line
if args.path:
  path = pathlib.Path(args.path)
else:
  path = pathlib.Path('/var/log/')
if args.days:
  days = args.days
else:
  days = 7

search_file_older_than_x_days(path,days)
