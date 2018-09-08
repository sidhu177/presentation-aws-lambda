import json
import urllib
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    print(bucket)
    backup = 'novalugduplicatebucket'
    print(backup)
    object = event['Records'][0]['s3']['object']['key']
    print(object)
    #print(type(object))
    backup_response = s3.copy_object(Bucket=backup,Key=object, CopySource={"Bucket":bucket, "Key":object})
    print(backup_response)
    state = backup_response["ResponseMetadata"]["HTTPStatusCode"] 
    print(state)
    
    sns = boto3.client('sns')
    sns_resource = 'arn:aws:sns:us-east-1:929003018535:novalugs3tosns'
    sns.publish(
        TopicArn = sns_resource,
        Subject = 'New Object in your Bucket!',
        Message=('New object has been uploaded to your S3: '+ str(object))
        #PhoneNumber='+123456789'
)
    if state == 200:
        return "Successfully duplicated %s to %s" % (object, backup)
    else:
        return "Unable to duplicate object"

   
    return "The object should be duplicated"