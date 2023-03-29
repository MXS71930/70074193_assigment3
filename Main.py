import boto3
import json


sqs=boto3.resource('sqs')

queue=sqs.create_queue(
   QueueName="Assigment_queue"
    
    
)