import re
import csv
import argparse
from collections import Counter

IP_REGEX = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# Create the parser
parser = argparse.ArgumentParser(description='Parse a log file and output IP address occurrences to a CSV file.')
parser.add_argument("--l", "--logfile",
                    help='Logfile to parse',
                    dest="logfile",
                    type=argparse.FileType('r'),
                    required=True)
parser.add_argument("--o", "--output",
                    help='Output CSV file name',
                    dest="outputfile",
                    type=str,
                    default="ip_count.csv")

def extract_ips(logfile):
    """Extracts all IP addresses from the given logfile."""
    return re.findall(IP_REGEX, logfile.read())

def count_ips(ip_list):
    """Count the occurrence of each IP address in the list."""
    return Counter(ip_list)

def write_csv(counter, filename):
    """Write the counter data to a CSV file."""
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["IP_Address", "Count"])
        writer.writeheader()
        for item, count in counter.items():
            writer.writerow({"IP_Address": item, "Count": count})
    print(f"IP counts written to {filename}")

def main():
    args = parser.parse_args()
    ip_list = extract_ips(args.logfile)
    ip_counter = count_ips(ip_list)
    write_csv(ip_counter, args.outputfile)

if __name__ == '__main__':
    main()
