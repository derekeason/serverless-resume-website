import simplejson as json
import boto3


dynamodb = boto3.client('dynamodb')
def lambda_handler(event, context):
    response = dynamodb.update_item(
        TableName='statistics',
        Key={
            'Site': {
                'N': '0'
            }
        },
        UpdateExpression='ADD #counter :increment',
        ExpressionAttributeNames={'#counter': 'visits'},
        ExpressionAttributeValues={':increment': {'N': '1'}
        },
        ReturnValues="UPDATED_NEW"
    )
    res = dynamodb.get_item(
        TableName='statistics',
        Key={
            'Site': {
                'N': '0'
            }
        },
        ProjectionExpression='visits',
    )
    count = response['Attributes']['visits']['N']
    print(res)
    vCount = int(count)
    return {
        'statusCode': 200,
        'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'        
        },
        'body': json.dumps(vCount)
        }
