import boto3
from passwordHash import hash_password

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

# Take user input
username = input("Enter your actual name: ")
user_id = input("Enter your user ID: ")
password = input("Enter your password: ")

# Hash the user ID and password
hashed_user_id = hash_password(user_id)
hashed_password = hash_password(password)

# Store the data in DynamoDB
response = table.put_item(
    Item={
        'username': username,
        'hashed_user_id': hashed_user_id,
        'hashed_password': hashed_password
    }
)

print("User information stored successfully.")
