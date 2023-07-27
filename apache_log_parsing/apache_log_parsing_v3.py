import re
import csv
import argparse
from collections import Counter

IP_REGEX = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# Create the parser
parser = argparse.ArgumentParser(description='Reading the log and CSV file')
parser.add_argument("--l", "--logfile",
                    help='Please enter the logfile to parse',
                    dest="logfile",
                    type=argparse.FileType('r'),
                    required=True)

def extract_ips(logfile):
    """Extracts all IP addresses from the given logfile."""
    try:
        with open(logfile, 'r') as f:
            log = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    return re.findall(IP_REGEX, log)

def count_ips(ip_list):
    """Count the occurrence of each IP address in the list."""
    return Counter(ip_list)

def write_csv(counter):
    """Write the counter data to a CSV file."""
    try:
        with open("ip_count.csv", 'w') as f:
            writer = csv.DictWriter(f, fieldnames=["IP_Address", "Count"])
            writer.writeheader()
            for item, count in counter.items():
                writer.writerow({"IP_Address": item, "Count": count})
    except Exception as e:
        print(f"Error writing CSV file: {e}")

def main():
    args = parser.parse_args()
    ip_list = extract_ips(args.logfile)
    ip_counter = count_ips(ip_list)
    write_csv(ip_counter)

if __name__ == '__main__':
    main()
