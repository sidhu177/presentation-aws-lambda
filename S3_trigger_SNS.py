import json
import boto3
import os

print("starting invocation")

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    print(bucket)
    region = event['Records'][0]['awsRegion']
    print(region)
    object = event['Records'][0]['s3']['object']['key']
    print(object)

    sns = boto3.client('sns')
    TopicArn = 'arn:aws:sns:us-east-1:929003018535:novalugs3tosns'
    Protocol = 'email'
    Endpoint = 'example@email.com'
    sns.subscribe(TopicArn,Protocol,Endpoint)
    sns.publish(
        Message=('New object has been uploaded to your S3: '+ str(object)), 
        PhoneNumber='+123456789'
)
    return "you should get a text message"
