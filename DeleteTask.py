import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ToDoTasks')

def lambda_handler(event, context):
    try:
        task_id = event['pathParameters']['id']

        table.delete_item(Key={'TaskID': task_id})

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': 'Task deleted'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }
