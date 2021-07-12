import paramiko
import time
import os

password=os.environ.get('PASSWORD')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='44.X.X.X',username='centos',password=password) # export the password export PASSWORD='<your password>' in the shell
stdin,stdout,stderr = ssh.exec_command('free -m')
time.sleep(5)
print(stdout.readlines())
ssh.close()
