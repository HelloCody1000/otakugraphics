import boto3

# Initialize a boto3 client
dynamodb = boto3.client('dynamodb')

# Define table creation parameters
table_name = 'UserCred'
key_schema = [
    {
        'AttributeName': 'hashed_user_id',
        'KeyType': 'HASH'  # partition key
    }
]
attribute_definitions = [
    {
        'AttributeName': 'hashed_user_id',
        'AttributeType': 'S'  # String
    }
]
provisioned_throughput = {
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}

# Create the table
try:
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attribute_definitions,
        ProvisionedThroughput=provisioned_throughput
    )

    # Wait for the table to be created
    print(f"Creating table {table_name}, please wait...")
    waiter = dynamodb.get_waiter('table_exists')
    waiter.wait(TableName=table_name)

    print(f"Table {table_name} created successfully.")
except Exception as e:
    print(f"Error creating table: {e}")
