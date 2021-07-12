#!/opt/anaconda3/bin/python

## Modules
import getpass
import paramiko

server = input("Enter the server name : ")
user = input("Enter the user name : ")
passwd = getpass.getpass()

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

## Connect to the server
try:
  ssh.connect(hostname=server, username=user, password=passwd)
except:
  print("[!] Cannot connect to the SSH Server")
  exit()

## Executing the commands
stdin, stdout, stderr = ssh.exec_command('ls -l')

print(stdout.read().decode())
