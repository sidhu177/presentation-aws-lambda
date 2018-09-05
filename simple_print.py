#simple print, also configure the event

import json

def lambda_handler(event,context):
    
    print('message to be printed '+ event['message'])
    return event['message']
    
