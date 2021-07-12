#!/opt/anaconda3/bin/python

## Modules
import getpass

user = getpass.getuser()

if user == "ahamedm" :
  print("I am the admin\nI can install software\nI can create user")
else:
  print("I dont have enough permission")
