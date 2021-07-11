import re
from collections import Counter
import csv
import argparse


logreg="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# Create the parser
my_parser = argparse.ArgumentParser(description='Reading the log and csv file')
my_parser.add_argument("--l","--logfile",
                       help='Please enter the logfile to parse',dest="logfile",type=argparse.FileType('r'), required=True)
args = my_parser.parse_args()


def read_file(logfile):
    with args.logfile as f:
        log = f.read()
        ip_list = re.findall(logreg,log)
        return ip_list

def read_count():
    ip_list = read_file(args.logfile)
    ip_count = Counter(ip_list)
    return ip_count.items()


def csv_write():
    counter = read_count()
    with open("ip_count.csv",'w') as f:
        fwriter = csv.writer(f)

        fwriter.writerow(["IP_Address","Count"])
        for item,val in counter:
            fwriter.writerow([item, val])

if __name__ == '__main__':
    csv_write()
