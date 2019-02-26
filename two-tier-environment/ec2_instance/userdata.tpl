#!/bin/bash
yum -y install httpd
service httpd start
chkconfig httpd on