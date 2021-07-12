import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='<ip address of remote host>',username='centos',password='<password>')
stdin,stdout,stderr = ssh.exec_command('free -m')
time.sleep(5)
print(stdout.readlines())
ssh.close()
