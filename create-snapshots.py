import boto3

client = boto3.client('ec2')

snsClient = boto3.client('sns')

# Get all volume ids for creating snapshots

volResp = client.describe_volumes()

volumeIds = []
snapshotIds = []
for vol in volResp['Volumes']:
    print(vol['VolumeId'])
    volumeIds.append(vol['VolumeId'])
    # Create snapshot
    snapResp = client.create_snapshot(
        VolumeId = vol['VolumeId'],
        Description = "Boto3"+vol['VolumeId']
    )
    snapshotIds.append(snapResp['SnapshotId'])

# Send email using SNS with volume ids and snapshot ids

email_body = """
   Volume IDs {}
   Snapshot Ids {}
"""

snsClient.publish(
    TopicArn='arn:aws:sns:ap-south-1:288621183532:volumes',
    Message=email_body.format(volumeIds,snapshotIds),
    Subject='EBS Snapshots Alert',
)
