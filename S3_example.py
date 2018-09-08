import json
import urllib
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    print(bucket)
    backup = 'novalugduplicatebucket'
    print(backup)
    key = event['Records'][0]['s3']['object']['key']
    print(key)
    #print(type(key))
    backup_response = s3.copy_object(Key=key, Bucket=backup, CopySource={"Bucket":bucket, "Key":key})
    print(backup_response)
    state = backup_response["ResponseMetadata"]["HTTPStatusCode"] 
    if state == 200:
        return "Successfully duplicated %s to %s" % (key, backup)
    else:
        return "Unable to duplicate object"
    
    return "The object should be duplicated"