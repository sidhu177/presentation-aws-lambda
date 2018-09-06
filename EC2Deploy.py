import boto3

REGION = 'us-east-1' # region 
AMI = 'ami-6871a115' # RED HAT AMI
INSTANCE_TYPE = 't2.micro' # instance type
EC2 = boto3.client('ec2', region_name=REGION)

def lambda_handler(event, context):
    instance = EC2.run_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        MinCount=1, # required by boto, even though it's kinda obvious.
        MaxCount=1,
        InstanceInitiatedShutdownBehavior='terminate', # make shutdown in script terminate ec2
    )

    print("New instance created.")
    instance_id = instance['Instances'][0]['InstanceId']
    print(instance_id)
    return instance_id