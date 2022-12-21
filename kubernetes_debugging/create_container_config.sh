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
  status=$(kubectl describe pod "$pod" -n "$namespace" | grep "CreateContainerConfigError" | awk '{print $2}')
  # If the status of the pod contains the "CreateContainerConfig" error
  if [[ "$status" = "CreateContainerConfigError" ]]; then
    # Print an error message
    echo "ERROR: Pod $pod has a CreateContainerConfig error!"
    exit 1

    # In some cases,Try to delete the pod to allow it to be rescheduled
    # kubectl delete pod "$pod" -n "$namespace"
  fi
done