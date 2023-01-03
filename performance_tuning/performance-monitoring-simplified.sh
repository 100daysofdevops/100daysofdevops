#!/bin/bash
# This script is the quick check to detect whether the performance issue is due to CPU, Memory, Input/Output (I/O), and network error 
# This script should work on both CentOS and macOS
# Author: Prashant Lakhera(laprashant@gmail.com)


# Check if the load average is greater than 70% of the CPU cores
load_avg=$(w | head -n 1 | awk '{print $9}' |cut -f1 -d",")
num_cores=$(nproc)
max_load=$(echo "0.7 * $num_cores" | bc)

if [[ $(echo "$load_avg > $max_load" | bc) -eq 1 ]]; then
  #Print a message if the load average is too high
  echo -e "\033[1;31m CPU load average is currently $load_avg, which is higher than the maximum of $max_load \033[0m" >&2
else
  # Print a  message if the load average is within the acceptable range
  echo -e "\033[1;32m CPU load average is currently $load_avg, which is within the acceptable range.\033[0m"
fi

# Set the memory average threshold
THRESHOLD=90

# Get the total memory and used memory in bytes
total_memory=$(grep 'MemTotal' /proc/meminfo | awk '{print $2}')
available_memory=$(grep 'MemAvailable' /proc/meminfo | awk '{print $2}')

# Calculate the actual memory utilization as a percentage
memory_utilization=$(echo "scale=2; ($total_memory - $available_memory)/$total_memory * 100" | bc)

# Compare the memory utilization with the threshold
if (( $(echo "$memory_utilization > $THRESHOLD" | bc -l) ))
then 
    echo -e "\033[1;32m Memory utilization is above the threshold!!! Memory utilization is: $utilization% \033[0m"
else
    echo -e "\033[1;32m Memory utilizationis currently $memory_utilization, which is within the acceptable range.\033[0m"
fi 

# Check the I/O wait state 

iowait_state=$(top -b -n 1 | head -n +3|awk '{print $10}'|tail -1 |bc)
if [[ $(echo "$iowait_state > 1" | bc) -eq 1 ]]; then
  #Print a message IOWAIT is too high
  echo -e "\033[1;31m IOWAIT is currently $iowait_state, which is higher than the acceptable range \033[0m" >&2
else
  # Print a  message IOWAIT is within the acceptable range
  echo -e "\033[1;32m IOWAIT is currently $iowait_state, which is within the acceptable range.\033[0m"
fi

# Check if ifconfig command is present
if command -v ifconfig >/dev/null 2>&1; then
  echo "ifconfig command is present"
else
  echo "ifconfig command is not present. Installing..."
  # Install ifconfig command
  if [ -f /etc/centos-release ]; then
    # CentOS
    sudo yum install -y net-tools
  elif [ -f /etc/lsb-release ]; then
    # Ubuntu
    sudo apt-get update
    sudo apt-get install -y net-tools
  else
    # Unsupported OS
    echo "Unsupported operating system"
    exit 1
  fi
fi

#Get the network interface name or ask input from the user
#interface=$1
interface=$(ifconfig |head -1|awk '{print $1}' |cut -f1 -d:)

# Get the RX error count
rx_error_count=$(ifconfig $interface | grep "RX errors" |awk '{print $3}')

# Get the TX error count
tx_error_count=$(ifconfig $interface | grep "TX errors" |awk '{print $3}')

# Check if either error count is greater than zero
# Remember these counter only get reset after reboot, so you may get some false alarm. Check this thread for more reference https://unix.stackexchange.com/questions/164057/how-can-i-manually-reset-rx-tx-counters-in-ifconfig-output-without-impacting-d 
if [[ $rx_error_count -gt 0 || $tx_error_count -gt 0 ]]; then
  #Print a message Network error count is too high
  echo -e "\033[1;31m Network Error is currently for Revieve Error: $rx_error_count and Transmit Error: $tx_error_count, which is higher than the acceptable range \033[0m" >&2
else
  # Print a  message Network error count is within the acceptable range
  echo -e "\033[1;32m Network Error is currently for Revieve Error: $rx_error_count and Transmit Error: $tx_error_count, which is within the acceptable range.\033[0m"
fi