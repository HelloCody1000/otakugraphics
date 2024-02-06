import boto3

# Initialize a DynamoDB client
dynamodb = boto3.resource('dynamodb')

# Define the table schema
table_name = 'clientInfo'
table_schema = {
    'TableName': table_name,
    'KeySchema': [
        {
            'AttributeName': 'user_id',  # Partition key
            'KeyType': 'HASH'  # Partition key is identified by HASH
        }
    ],
    'AttributeDefinitions': [
        {
            'AttributeName': 'user_id',
            'AttributeType': 'S'  # 'S' stands for string
        }
        # Note: 'password' and 'type' are not part of the key schema,
        # so they are not listed in AttributeDefinitions
    ],
    'ProvisionedThroughput': {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
}

# Create the table
try:
    table = dynamodb.create_table(**table_schema)
    table.wait_until_exists()
    print(f"Table {table_name} created successfully.")
except Exception as e:
    print(f"Error creating table: {e}")
