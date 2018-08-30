import boto3
import os

def lambda_handler(event, context):
    sns = boto3.client('sns')
    sns.publish(
        Message=('Hello From NovaLUG'), 
        PhoneNumber='+123456789'
)
    return "you should get a text message"
