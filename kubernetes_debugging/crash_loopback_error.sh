#!/bin/bash
# Script to check Crashloopbackoff error in Kubernetes pods
# Author: Prashant Lakhera(laprashant@gmail.com)

# Set the namespace which we use to query the pods
namespace="default"

# Query for the pods using the namespace
pods=$(kubectl get pods -n "$namespace" -o json | jq -r '.items[].metadata.name')

# Iterate through the list of pods
for pod in $pods; do
  # Get the status of the current pod
  status=$(kubectl describe pod "$pod" -n "$namespace"| grep "CrashLoopBackOff" |awk '{print $2}')

  # If the status is "CrashLoopBackOff", handle the error
  for state in status
  do 
    if [ "$status" == "CrashLoopBackOff" ]; then
    # Print an error message
        echo "ERROR: Pod $pod is in a CrashLoopBackOff state!"
        exit 1

        # Try to delete the pod to allow it to be rescheduled
        #kubectl delete pod "$pod" -n "$namespace"

        # Print a message indicating that the pod was deleted
        #echo "INFO: Deleted pod $pod to allow it to be rescheduled."
    fi
  done  
done
