import boto3

# Defining the EC2
REGION = 'us-east-1' # region to launch instance.
AMI = 'ami-6871a115'  # Red Hat Image
INSTANCE_TYPE = 't2.micro' # instance type to launch.
SG = 'sg-02e28977'  # Default Security Group
EC2Key = 'AWSKeyPair' # Key Pair
EC2 = boto3.client('ec2', region_name=REGION)

# installing an Apache Server
init_script = """#!/bin/bash
sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd.service
"""

def lambda_handler(event, context):

 
def lambda_handler(event, context):
    
    state = event['detail']['state']
    
    if state == ['terminated']:
       instance = EC2.run_instances(
           ImageId=AMI,
           InstanceType=INSTANCE_TYPE,
           MinCount=1, # required by boto, even though it's kinda obvious.
           MaxCount=1,
           InstanceInitiatedShutdownBehavior='terminate', # make shutdown in script terminate ec2
           KeyName = EC2Key,
           SecurityGroupIds = [SG],
           UserData=init_script 
        )

    print("New instance created.")
    instance_id = instance['Instances'][0]['InstanceId']
    print(instance_id)

    return instance_id