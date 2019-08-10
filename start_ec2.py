import boto3

client = boto3.client('ec2')

client.start_instances(
    InstanceIds=["i-0ed36db7bb96570bf"]
)