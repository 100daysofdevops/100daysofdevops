#!/usr/bin/env python3
import os

# Function to list top 5 CPU consuming processes
def list_top_cpu_consuming_processes():
    # Get the top 5 processes by CPU usage
    top_five_cpu_processes = os.popen("ps -eo pcpu,pid,user,args | sort -k 1 -r | head -n 6").read()

    # Print the results
    print("###############################################################################")
    print("Top 5 CPU consuming processes:")
    print(top_five_cpu_processes)

# Function to list the top 5 processes by memory usage
def list_top_memory_consuming_processes():
    # Get the top 5 processes by memory usage
    top_five_memory_processes = os.popen("ps -eo pmem,pid,user,args | sort -k 1 -r | head -n 6").read()

    # Print the results
    print("###############################################################################")
    print("Top 5 memory consuming processes:")
    print(top_five_memory_processes)

# Check if iotop command is present
if os.system("command -v iotop >/dev/null 2>&1") == 0:
    print("iotop command is present")
else:
    print("iotop command is not present. Installing...")
    # Install iotop command
    if os.path.isfile("/etc/centos-release"):
        # CentOS
        os.system("sudo yum install -y epel-release")
        os.system("sudo yum install -y iotop")
    elif os.path.isfile("/etc/lsb-release"):
        # Ubuntu
        os.system("sudo apt-get update")
        os.system("sudo apt-get install -y iotop")
    else:
        # Unsupported OS
        print("Unsupported operating system")
        exit(1)

# Function to list the top 5 processes by I/O usage
def list_top_io_consuming_processes():
    # Get the top 5 processes by I/O usage
    top_five_io_processes = os.popen("sudo iotop -o -b -n 6").read()

    # Print the results
    print("###############################################################################")
    print("Top 5 I/O consuming processes:")
    print(top_five_io_processes)

# Check if iftop command is present
if os.system("command -v iftop >/dev/null 2>&1") == 0:
    print("iftop command is present")
else:
    print("iftop command is not present. Installing...")
    # Install iftop command
    if os.path.isfile("/etc/centos-release"):
        # CentOS
        os.system("sudo yum install -y iftop")
    elif os.path.isfile("/etc/lsb-release"):
        # Ubuntu
        os.system("sudo apt-get update")
        os.system("sudo apt-get install -y iftop")
    else:
        # Unsupported OS
        print("Unsupported operating system")
        exit(1)

# Function to list the top 5 processes by network usage
def list_top_network_consuming_processes():
    # Get the top 5 processes by network usage
    top_five_network_processes = os.popen("sudo iftop -P -n -t -s 6").read()

    # Print the results
    print("###############################################################################")
    print("Top 5 network consuming processes:")
    print(top_five_network_processes)

# Main function
def main():
    list_top_cpu_consuming_processes()
    list_top_memory_consuming_processes()
    list_top_io_consuming_processes()
    list_top_network_consuming_processes()

# Run the main function
if __name__ == "__main__":
    main()
