import boto3

client = boto3.client('sns')

ses = boto3.client('ses')

response = client.create_topic(
    Name='my-test-topic')

response = client.subscribe(
    TopicArn='arn:aws:sns:us-west-2:XXXXXXXXX:my-test-topic',
    Protocol='email',
    Endpoint='102daysofdevops@gmail.com',
    ReturnSubscriptionArn=True
)

response = client.publish(TopicArn='arn:aws:sns:us-west-2:XXXXXX:my-test-topic',Message="Hello from aws")
print(response)

response = ses.send_email(
    Source=EMAIL_FROM,
    Destination={
        'ToAddresses': [EMAIL_TO]
    },
    Message={
        'Subject': {
            'Data': ('Cleanup following Volume  '
                     f'Volume: {vol_id}')
        },
        'Body': {
            'Text': {
                'Data': data
            }
        }
    })
