#!/home/vumile/python2.7/bin/python
import boto3
take_one=[]
info1=open('Output.html','r')
info2=open('Output2.html','r')
for i in info1:
 take_one.append(i)
for x in info2:
 take_one.append(x)
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='Node_info')
response = queue.send_message(MessageBody=(''.join(map(str,take_one))))
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))
info2.close()
info1.close()

