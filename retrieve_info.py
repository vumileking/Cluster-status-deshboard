#!/usr/bin/python
import boto3
import json
region_name = 'us-east-2'
queue_name = 'Node_info'
max_queue_messages = 1
message_bodies = []
aws_access_key_id = 'AKIAJSTLBB3RI63FUXSA'
aws_secret_access_key = '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'
sqs = boto3.resource('sqs', region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key)
queue = sqs.get_queue_by_name(QueueName=queue_name)
while True:
    messages_to_delete = []
    for message in queue.receive_messages(MaxNumberOfMessages=max_queue_messages):
        # process message body
        body = message.body
        message_bodies.append(body)
        # add message to delete
        messages_to_delete.append({
            'Id': message.message_id,
            'ReceiptHandle': message.receipt_handle
      })
    if len(message_bodies)>0:
     translator=open("index.html", "w")
     translator.write(''.join(map(str,message_bodies[0:1])))
     translator.close()
    # if you don't receive any notifications the
    # messages_to_delete list will be empty
    if len(messages_to_delete) == 0:
        break
    # delete messages to remove them from SQS queue
    # handle any errors
    else:
        delete_response = queue.delete_messages(
                Entries=messages_to_delete)

