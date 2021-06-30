import os
import datetime

currentdate=datetime.datetime.now()
max_age=15

for dirpath, dirname, filename in os.walk("/etc/openldap"):
    for file in filename:
        comp_path= os.path.join(dirpath,file)
        file_stat=os.stat(comp_path)
        file_ctime = file_stat.st_ctime
        file_creation_in_days= datetime.datetime.fromtimestamp(file_ctime)
        diff_in_days=(currentdate - file_creation_in_days).days
        if diff_in_days > max_age:
            print(comp_path, diff_in_days)
