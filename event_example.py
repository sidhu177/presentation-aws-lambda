import time

def lambda_handler(event,context):
    calc = 2**3**2
    print(calc)
    print("Remaining Time in MilliSeconds: " + str(context.get_remaining_time_in_millis()))
    calc = 2**5**7
    print(calc)
    print("Remaining Time in MilliSeconds: " + str(context.get_remaining_time_in_millis()))
    calc = 3**5**7
    print(calc)
    print("Remaining Time in MilliSeconds: " + str(context.get_remaining_time_in_millis()))
    print("This is the RequestID: " + str(context.aws_request_id))
    return "End of Lambda Function"