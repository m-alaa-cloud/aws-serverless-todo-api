import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ToDoTasks')

def lambda_handler(event, context):
    try:
        task_id = event['pathParameters']['id']
        data = json.loads(event['body'])

        update_expression = "SET "
        expression_values = {}
        expression_names = {}

        if 'taskName' in data:
            update_expression += "#name = :name, "
            expression_values[':name'] = data['taskName']
            expression_names['#name'] = 'taskName'

        if 'status' in data:
            update_expression += "#status = :status, "
            expression_values[':status'] = data['status']
            expression_names['#status'] = 'status'

        if not expression_values:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'error': 'No valid fields provided for update'})
            }

        update_expression = update_expression.rstrip(', ')

        update_args = {
            'Key': {'TaskID': task_id},
            'UpdateExpression': update_expression,
            'ExpressionAttributeValues': expression_values
        }

        if expression_names:
            update_args['ExpressionAttributeNames'] = expression_names

        table.update_item(**update_args)

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': 'Task updated successfully'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }
