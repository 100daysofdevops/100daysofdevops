#!/bin/bash
# Script to check ContainerCreating error in Kubernetes pods
# Author: Prashant Lakhera(laprashant@gmail.com)

# Set the namespace which we use to query the pods
namespace="default"

# Query for the pods using the namespace
pods=$(kubectl get pods -n "$namespace" -o json | jq -r '.items[].metadata.name')

# Iterate through the list of pods
for pod in $pods; do
  # Get the status of the current pod
  status=$(kubectl get pod "$pod" -n "$namespace" -o json | jq -r '.status.containerStatuses[].state.waiting.reason')
  # Check if the status is "ContainerCreating"
  if [ "$status" == "ContainerCreating" ]; then
    # Print an error message
    echo "ERROR: Pod $pod is in a ContainerCreating state!"
    exit 1
    # In some cases this is helpful,try to delete the pod to allow it to be rescheduled
    # kubectl delete pod "$pod" -n "$namespace"
  fi
done    


