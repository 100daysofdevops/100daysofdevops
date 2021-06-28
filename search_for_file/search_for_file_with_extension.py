import os
import argparse

my_parser = argparse.ArgumentParser(description='Reading the directory path to find the file')
my_parser.add_argument("pathname",
                        help='Please enter the directory path ')
args = my_parser.parse_args()

for dirname, dirpath, filename in os.walk(args.pathname):
    for file in filename:
        if file.endswith('.conf'):
            print(os.path.join(dirname,file))



