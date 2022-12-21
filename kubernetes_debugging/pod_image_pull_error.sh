#!/bin/bash
# Script to check image pull error in Kubernetes pods
# Author: Prashant Lakhera(laprashant@gmail.com)

# Set the namespace which we use to query the pods
NAMESPACE=default

# Query for the pods using the namespace and label selector
PODS=$(kubectl get pods -n $NAMESPACE -o json)

# Verify if the query return any pods
if [ -z "$PODS" ]; then
  echo "No pods found"
  exit 0
fi

# Parse the JSON output to get the list of pod names
POD_NAMES=$(echo $PODS | jq -r '.items[].metadata.name')

# Iterate over the list of pod names
for POD_NAME in $POD_NAMES; do
    # Check for image pull errors in the pod
    IMAGE_PULL_ERRORS=$(kubectl describe pod $POD_NAME -n $NAMESPACE | grep -c "ImagePullBackOff")

    # If there is a image pull errors, print an error message and exit with an error code
    if [ "$IMAGE_PULL_ERRORS" -gt 0 ]; then
      echo "There were image pull errors in pod $POD_NAME"
    fi  
done

# If there is no image pull error and all the pods are running, exit with a zero status code
exit 0