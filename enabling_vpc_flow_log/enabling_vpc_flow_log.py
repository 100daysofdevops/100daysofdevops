import boto3
from botocore.exceptions import ClientError


client = boto3.client("ec2")
client_log = boto3.client('logs')


for vpcid in client.describe_vpcs()['Vpcs']:
    vpc_id = vpcid['VpcId']
    print(vpc_id)

    log_group = vpc_id + "-flowlog" 

    try:
        response = client_log.create_log_group(
            logGroupName=log_group)
    except ClientError:
            print("Log group already exist for the following vpc: ", vpc_id)

    flow_log_filter={"Name":"resource-id","Values":[vpc_id]}
    response = client.describe_flow_logs(Filters=[flow_log_filter])
    if len(response['FlowLogs']) > 0:
        print("VPC Flowlog is already enabled for this VPC: ", vpc_id)
    else:
        print("Enabling Flow logs for the following VPC: ")
        response = client.create_flow_logs(
            ResourceIds=[vpc_id],
            ResourceType='VPC',
            TrafficType='ALL',
            LogGroupName=log_group,
            DeliverLogsPermissionArn="<arn for your IAM Role>"
        )
