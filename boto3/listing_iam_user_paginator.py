import boto3

iam_client = boto3.client("iam")
paginator = iam_client.get_paginator('list_users')
page_iterator=paginator.paginate()
count=1
for user in page_iterator:
    for username in user['Users']:
        print(count, username['UserName'])
        count+=1
