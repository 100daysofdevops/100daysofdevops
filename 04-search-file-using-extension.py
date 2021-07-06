#!/opt/anaconda3/bin/python3

##  Modules
import pathlib
import argparse

def search_file_using_extension(path,ext):
  for file in path.iterdir():
    if file.name.endswith(ext):
      print("The file %s ends with the %s extension"%(file,ext))
  
def path_exist(path,ext):
  path = pathlib.Path(path)
  if path.exists():
    search_file_using_extension(path,ext)
  else:
    print("The path doesnt exist")

## Create the parser
parser = argparse.ArgumentParser()

## Add the arguments
parser.add_argument("--path", help="Directory Path to search for files")
parser.add_argument("--ext", help="mention the extension to search for files")

## Execute the parse_arg() method
args = parser.parse_args()

path_exist(args.path,args.ext)
