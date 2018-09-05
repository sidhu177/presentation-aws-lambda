#simple print, also configure the event

import json
import os

# val =  os.environ['Key1']

def lambda_handler(event,context):
    
    print('message to be printed '+ event['message'])
    # print(val)
    return event['message']
    
