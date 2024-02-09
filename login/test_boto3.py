import boto3
from botocore.exceptions import NoCredentialsError

# Initialize a DynamoDB client
dynamodb = boto3.client('dynamodb')

try:
    # List DynamoDB tables
    response = dynamodb.list_tables()
    print("DynamoDB Tables:", response['TableNames'])
except NoCredentialsError:
    print("Credentials not available")
except Exception as e:
    print("Error:", e)
