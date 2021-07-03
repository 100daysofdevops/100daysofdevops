import os
import argparse

my_parser = argparse.ArgumentParser(description='Reading the directory path to find the file')
my_parser.add_argument("--p","--pathname",
                        help='Please enter the directory path ')
my_parser.add_argument("--f","--filesearch",
                      help='Please enter the filename to search')
args = my_parser.parse_args()

for dirpath, dirname, filename in os.walk(args.pathname):
    for file in filename:
        comp_path= os.path.join(dirpath,file)
        if file == args.filesearch:
            print(comp_path)
