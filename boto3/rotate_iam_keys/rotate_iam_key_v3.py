import boto3
from datetime import datetime, timezone

client = boto3.client("iam")
s3 = boto3.client("s3")
paginator = client.get_paginator('list_users')

max_key_age = 5
s3_bucket = "my-bucket-name"
s3_key_prefix = "new-keys/"

def rotate_key(key_creation_date):
    current_date = datetime.now(timezone.utc)
    age = (current_date - key_creation_date).days
    return age

for response in paginator.paginate():
    for user in response['Users']:
        username = user['UserName']

        # Create a new access key for the user
        response = client.create_access_key(UserName=username)
        access_key_id = response['AccessKey']['AccessKeyId']
        secret_access_key = response['AccessKey']['SecretAccessKey']

        # Upload the new access key to an S3 bucket(Please do it at your own risk)
        s3_key = f"{s3_key_prefix}{access_key_id}.txt"
        s3.put_object(
            Bucket=s3_bucket,
            Key=s3_key,
            Body=f"Access Key ID: {access_key_id}\nSecret Access Key: {secret_access_key}"
        )

        listkey = client.list_access_keys(UserName=username)
        for accesskey in listkey['AccessKeyMetadata']:
            accesskey_id = accesskey['AccessKeyId']
            key_creation_date = accesskey['CreateDate']
            age = rotate_key(key_creation_date)
            if age > max_key_age:
                print(f"Deactivating key for the following user: {username}")
                client.update_access_key(UserName=username, AccessKeyId=accesskey_id, Status='Inactive')
