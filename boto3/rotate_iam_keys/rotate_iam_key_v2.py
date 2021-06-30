import boto3
from datetime import datetime, timezone


client = boto3.client("iam")
paginator = client.get_paginator('list_users')

max_key_age=5

def rotate_key(key_creation_date):
    current_date = datetime.now(timezone.utc)
    age = (current_date - key_creation_date).days
    return age

for response in paginator.paginate():
    for user in response['Users']:
        username = user['UserName']

        listkey = client.list_access_keys(
                UserName=username)
        for accesskey in listkey['AccessKeyMetadata']:
            accesskey_id = accesskey['AccessKeyId']
            key_creation_date = accesskey['CreateDate']
            age = rotate_key(key_creation_date)
            if age > max_key_age:
                print("Deactivating Key for the following users: " + username)
                client.update_access_key(UserName=username, AccessKeyId=accesskey_id, Status='Inactive')
