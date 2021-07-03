#!/opt/anaconda3/bin/python3

## Modules
import pathlib
import argparse

## Function
def file_search(dir,file):
  try:
    if dir.is_dir():
      #print("Directory exists")
      if file.is_file():
        print("The file %s exist in the %s directory" %(args.arg2,args.arg1))
      else:
        print("The dir %s exist but the file %s is not in the directory" %(args.arg1,args.arg2))
    else:
      print("The directory %s doesnt exist" %args.arg1)
  except:
    print("Something went wrong")


## Create the parser
parser = argparse.ArgumentParser()

## Add the arguments
parser.add_argument("arg1", help="Directory Name")
parser.add_argument("arg2", help="File Name to search for in the dir")

## Execute the parse_arg() method
args = parser.parse_args()

dir = pathlib.Path(args.arg1)
file = pathlib.Path(args.arg1,args.arg2)

file_search(dir,file)
