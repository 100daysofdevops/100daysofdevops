import boto3
from datetime import datetime, timezone


client = boto3.client("iam")
sns = boto3.resource("sns")
paginator = client.get_paginator('list_users')
current_date=datetime.now(timezone.utc)
max_key_age=5

for response in paginator.paginate():
    for user in response['Users']:
        username = user['UserName']

        listkey = client.list_access_keys(
                UserName=username)
        for accesskey in listkey['AccessKeyMetadata']:
            accesskey_id = accesskey['AccessKeyId']
            key_creation_date = accesskey['CreateDate']
            age = (current_date - key_creation_date).days

            if age > max_key_age:
                print("Deactivating Key for the following users: " + username)
                client.update_access_key(UserName=username, AccessKeyId=accesskey_id, Status='Inactive')
