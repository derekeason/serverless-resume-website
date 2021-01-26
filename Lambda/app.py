import json
import boto3
import os

# Initialize dynamodb boto3 object
dynamodb = boto3.resource('dynamodb')
# Set dynamodb table name variable from env
ddbTableName = os.environ['databaseName']
table = dynamodb.Table(ddbTableName)

def lambda_handler(event, context):
    # Update item in table or add if doesn't exist
    ddbResponse = table.update_item(

        Key={
            'siteUrl': '{"S":"https://www.derekeason.io"}, "visits": {"N": "0"}'
        },
        UpdateExpression='SET visits = visits + :value',
        ExpressionAttributeValues={
            ':value': {'N": '1'}
        },
        ReturnValues="UPDATED_NEW"

    )
    print("UPDATING ITEM")
    print(response)

    #import boto3dynamodb = boto3.client('dynamodb')response = dynamodb.update_item
    #(    TableName='siteVisits',     Key={        'siteUrl':{'S': "https://www.linuxacademy.com/"}    },
    #  UpdateExpression='SET visits = visits + :inc',    ExpressionAttributeValues={        ':inc': {'N': '1'}    },
    # ReturnValues="UPDATED_NEW")print("UPDATING ITEM")print(response)
    # # Format dynamodb response into variable
    # responseBody = json.dumps({"HelloThere": ddbResponse["Attributes"]["generalle"]})
    #
    # # Create api response object
    # apiResponse = {
    #     "isBase64Encoded": False,
    #     "statusCode": 200,
    #     "body": responseBody
    # }
    #
    # # Return api response object
    # return apiResponse
