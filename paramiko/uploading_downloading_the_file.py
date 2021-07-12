import paramiko
import time
import os

password = os.environ.get('PASSWORD')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='44.X.X.X',username='centos',password=password)

ftp_client=ssh.open_sftp()
ftp_client.put('myls.py','myls.py')
ftp_client.get('myls.py','/tmp/myls.py')

ftp_client.put('myls.py','myls.py')
ftp_client.close()
