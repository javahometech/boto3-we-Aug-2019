import json
import boto3
snsClient = boto3.client('sns')
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    ec2_id = event['detail']['instance-id']
    ec2_state = event['detail']['state']
    instance = ec2.Instance(ec2_id)
    instance_name = None
    for tag in instance.tags:
        if tag['Key'] == 'Name':
            instance_name = tag['Value']
            break
            
    email_body = f"""
      Hi Team, 
      EC2 Instance ID {ec2_id},
      ECS Instance Name {instance_name}
      is changing its state to {ec2_state}
    
    """
    
    snsClient.publish(
        TopicArn = 'arn:aws:sns:ap-south-1:288621183532:volumes',
        Subject = 'EC2 Is stopping',
        Message = email_body
    )
    
