import boto3

REGION = 'us-east-1' # region to launch instance.
AMI = 'ami-6871a115'  # Red Hat Image
INSTANCE_TYPE = 't2.micro' # instance type to launch.
SG = 'sg-02e28977'  # Default Security Group
EC2Key = 'AWSKeyPair' # Kay Pair
EC2 = boto3.client('ec2', region_name=REGION)

init_script = """#!/bin/bash
sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd.service
"""

def lambda_handler(event, context):
    
    state = event["detail"]["state"]
    print(state)
    if state==["terminated"] or state=='terminated':
       instance = EC2.run_instances(
       ImageId=AMI,
       InstanceType=INSTANCE_TYPE,
       MinCount=1, 
       MaxCount=1,
       InstanceInitiatedShutdownBehavior='terminate', 
       KeyName = EC2Key,
       SecurityGroupIds = [SG],
       UserData=init_script )
    else:
       print("its all good!")
       
    print("New instance created.")
    instance_id = instance['Instances'][0]['InstanceId']
    print(instance_id)
    return instance_id
    
    