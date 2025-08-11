import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ToDoTasks')
sns = boto3.client('sns')


SNS_TOPIC_ARN = 'arn:aws:sns:eu-north-1:557690582558:taskEvents'

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
        task_id = str(uuid.uuid4())
        
        item = {
            'TaskID': task_id,
            'taskName': data.get('taskName', 'Untitled'),
            'status': data.get('status', 'pending')
        }

        table.put_item(Item=item)

         
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject='New Task Created',
            Message=f"Task '{item['taskName']}' was created with status '{item['status']}'."
        )

        return {
            'statusCode': 201,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': 'Task created', 'taskId': task_id})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }
