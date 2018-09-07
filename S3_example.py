
import json
import urllib
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    backup = bucket + "-backup"
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    backup_response = s3.copy_object(Key=key, Bucket=backup, CopySource={"Bucket":bucket, "Key":key})
    state = backup_response["ResponseMetadata"]["HTTPStatusCode"] 
    if state == 200:
         return "Successfully duplicated %s to %s" % (key, backup)
     else:
         return "Unable to duplicate object"
    
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}.'.format(key, bucket))
        raise e
