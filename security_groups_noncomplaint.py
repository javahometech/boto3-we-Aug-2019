"""
    Find security Groups with 22 open to internet
"""
import boto3

ec2 = boto3.resource('ec2')

securityGroups = ec2.security_groups.all()

for sg in securityGroups:
    for permissions in sg.ip_permissions:

        condition_one = 'IpProtocol' in permissions and permissions['IpProtocol'] == "-1"
        condition_two = 'FromPort' in permissions and permissions['FromPort'] == 22

        if condition_one or condition_two :
            for ip_ranges in permissions['IpRanges']:
                print(ip_ranges)
                if ip_ranges['CidrIp'] == '0.0.0.0/0':
                    print(f"Security Group {sg.group_name} is non compliant")

