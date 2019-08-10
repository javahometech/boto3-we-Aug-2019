import boto3

client = boto3.client('ec2')
eipResp = client.describe_addresses()
epips = []
for eip in eipResp['Addresses']:
   if 'InstanceId' not in eip:
       print('{} is not in use'.format(eip['PublicIp']))
       epips.append(eip['PublicIp'])

# Send email
