import json
import urllib
import boto3

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    backup = bucket + "-backup"
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    try:
        backup_response = s3.copy_object(Key=key, Bucket=backup, CopySource={"Bucket":bucket, "Key":key})
        if backup_response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return "Successfully copied %s to %s" % (key, backup)
        else:
            return "Unable to copy %s to %s: %s" % (key, backup, backup_response)
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
