import os
import datetime

file_age=15

def days_creation(file_creation_time):
    today_date = datetime.datetime.now()
    time_diff = (today_date - file_creation_time).days
    return time_diff


for dir,dirpath,filename in os.walk("/var/log"):
    for file in filename:
        complete_path=os.path.join(dir,file)
        file_creation_time=datetime.datetime.fromtimestamp(os.path.getctime(complete_path))
        time_diff = days_creation(file_creation_time)
        if time_diff> file_age:
            print(complete_path, time_diff)
