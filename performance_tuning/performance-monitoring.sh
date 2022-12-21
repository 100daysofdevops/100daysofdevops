#!/bin/bash
# This script list the top 5 CPU, memory, input/output (I/O), and network consuming processes
# This script should work on both CentOS and macOS
# Author: Prashant Lakhera(laprashant@gmail.com)

# Check if top command is present
if command -v top >/dev/null 2>&1; then
  echo "top command is present"
else
  echo "top command is not present. Installing..."
  # Install top command
  if [ -f /etc/centos-release ]; then
    # CentOS
    sudo yum install -y procps-ng
  elif [ -f /etc/lsb-release ]; then
    # Ubuntu
    sudo apt-get update
    sudo apt-get install -y procps
  else
    # Unsupported OS
    echo "Unsupported operating system"
    exit 1
  fi
fi

# Function to list top 5 CPU consuming process
list_top_cpu_consuming_processes() {
  # Get the top 5 processes by CPU usage
  top_five_cpu_processes=$(ps -eo pcpu,pid,user,args | sort -k 1 -r | head -n 5)

  # Print the results
  echo "###############################################################################"
  echo "Top 5 CPU consuming processes:"
  echo "$top_five_cpu_processes"
}

# Function to list the top 5 processes by memory usage
list_top_memory_consuming_processes() {
  # Get the top 5 processes by memory usage
  top_five_memory_processes=$(ps -eo pmem,pid,user,args | sort -k 1 -r | head -n 5)

  # Print the results
  echo "###############################################################################"
  echo "Top 5 memory consuming processes:"
  echo "$top_five_memory_processes"
}

# Check if iotop command is present
if command -v iotop >/dev/null 2>&1; then
  echo "iotop command is present"
else
  echo "iotop command is not present. Installing..."
  # Install top command
  if [ -f /etc/centos-release ]; then
    # CentOS
    sudo yum install -y epel-release
    sudo yum install -y iotop
  elif [ -f /etc/lsb-release ]; then
    # Ubuntu
    sudo apt-get update
    sudo apt-get install -y iotop
  else
    # Unsupported OS
    echo "Unsupported operating system"
    exit 1
  fi
fi

# Function to list the top 5 processes by I/O usage
list_top_io_consuming_processes() {
  # Get the top 5 processes by I/O usage
  top_five_io_processes=$(sudo iotop -o -b -n 5)

  # Print the results
  echo "###############################################################################"
  echo "Top 5 I/O consuming processes:"
  echo "$top_five_io_processes"
}

# Check if iftop command is present
if command -v iftop >/dev/null 2>&1; then
  echo "iftop command is present"
else
  echo "iftop command is not present. Installing..."
  # Install top command
  if [ -f /etc/centos-release ]; then
    # CentOS
    sudo yum install -y iftop
  elif [ -f /etc/lsb-release ]; then
    # Ubuntu
    sudo apt-get update
    sudo apt-get install -y iftop
  else
    # Unsupported OS
    echo "Unsupported operating system"
    exit 1
  fi
fi


# Function to list the top 5 processes by network usage
list_top_network_consuming_processes() {
  # Get the top 5 processes by network usage
  top_five_network_processes=$(sudo iftop -P -n -t -s 5)

  # Print the results
  echo "###############################################################################"
  echo "Top 5 network consuming processes:"
  echo "$top_five_network_processes"
}


# Main function
main() {
  list_top_cpu_consuming_processes
  list_top_memory_consuming_processes
  list_top_io_consuming_processes
  list_top_network_consuming_processes
}

# Run the main function
main
