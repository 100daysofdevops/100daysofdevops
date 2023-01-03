#!/bin/bash
# This shell script that checks if the required python modules (pip3, boto3, and awscli)
# the terraform package are installed, and installs them if they are missing. 
# This script should work on both CentOS and macOS
# Check the terraform release page to use the latest terraform package https://releases.hashicorp.com/terraform/
# Author: Prashant Lakhera(laprashant@gmail.com)

# Check if pip3 is installed
if ! type "pip3" &> /dev/null
then 
    echo "pip3 is not installed. Installing now ..."
    # Install pip3
    # Checking for Mac
    if [ "$(uname)" == "Darwin" ]
    then
        brew install python3
    # Checking for Centos
    elif [ -f /etc/centos-release ]
    then
        sudo yum -y update
        sudo yum -y install python3-pip -y
    fi
fi

# Check if boto3 is installed
if python3 -c "import boto3" &> /dev/null; then
    echo "Boto3 is already installed"
else
    echo "Boto3 is not installed. Installing now...."
    pip3 install boto3 --user
fi

# Check if awscli is installed
if ! type "aws" > /dev/null
then
    echo "awscli is not installed. Installing now..."
    pip3 install awscli --user
else
    echo "awscli is already installed"
fi

# Check if terraform is installed
if ! type "terraform" > /dev/null
then
    echo "terraform is not installed installing now..."
    # Install terraform
    #Checking for Mac
    if [ "$(uname)" == "Darwin" ]
    then
        brew install terraform
    # Checking for Centos
    elif [ -f /etc/centos-release ]
    then 
        sudo yum install -y unzip
        sudo wget https://releases.hashicorp.com/terraform/1.3.6/terraform_1.3.6_linux_amd64.zip
        sudo unzip terraform_1.3.6_linux_amd64.zip
        sudo mv terraform /usr/local/bin/
        sudo chmod +x /usr/local/bin/terraform
        sudo rm terraform_1.3.6_linux_amd64.zip
    fi    
else
    echo "Terraform is already installed"
    
fi            