import boto3

f = open("Config.txt", "r")



def sendMessage ():
    queue = sqs.get_queue_by_name(QueueName='Assigment_queue')
    response = queue.send_message(MessageBody='hello reyaan',MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'The Whistler'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'John Grisham'
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        }
    }
                              
)
    