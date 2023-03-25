import boto3
from datetime import datetime, timezone

client = boto3.client("iam")
paginator = client.get_paginator('list_users')

max_key_age = 5
excluded_users = ["user1", "user2"] # List of usernames to exclude

def rotate_key(key_creation_date):
    current_date = datetime.now(timezone.utc)
    age = (current_date - key_creation_date).days
    return age

for response in paginator.paginate():
    for user in response['Users']:
        username = user['UserName']

        if username in excluded_users:
            # Skip processing excluded users
            continue

        listkey = client.list_access_keys(UserName=username)
        for accesskey in listkey['AccessKeyMetadata']:
            accesskey_id = accesskey['AccessKeyId']
            key_creation_date = accesskey['CreateDate']
            age = rotate_key(key_creation_date)
            if age > max_key_age:
                print(f"Deactivating key for the following user: {username}")
                client.update_access_key(UserName=username, AccessKeyId=accesskey_id, Status='Inactive')
