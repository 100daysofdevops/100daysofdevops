#!/opt/anaconda3/bin/python

## Modules
import pathlib
import sys
import os
import subprocess

## Checking the path existance
path = pathlib.Path(sys.argv[1])
if path.exists():
  print(" Listing the file from the given directory %s"%sys.argv[1])
  subprocess.run("ls -la",shell=True)
else:
  print("Path %s doesnt exist"%sys.argv[1])
