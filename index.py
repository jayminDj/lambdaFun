import json

print('Loading function')
def my_handler(event,context):
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])
    print('Request Id - '+ context.aws_request_id)
    return event['key1']  # Echo back the first key value

