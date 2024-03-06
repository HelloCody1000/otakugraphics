import boto3
from bcrypt import hashpw, gensalt
import validators  # A library for validating data like emails

def create_user(username, user_id, password, email):
    # Validation (simplified examples)
    if not validators.email(email):
        raise ValueError("Invalid email format")
    if len(password) < 8:
        raise ValueError("Password too short")
    
    # Initialize DynamoDB connection
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('UserCred')
    
    # Check for existing user
    response = table.get_item(Key={'user_id': user_id})
    if 'Item' in response:
        raise ValueError("User ID already exists")
    
    # Hash password only
    hashed_password = hashpw(password.encode('utf-8'), gensalt())
    
    # Store user data
    try:
        table.put_item(Item={
            'username': username,
            'user_id': user_id,  # Consider storing user_id in plain text for easier querying
            'hashed_password': hashed_password.decode('utf-8'),  # Ensure the hashed password is stored in a storable format
            'email': email,  # Consider storing email in plain text for communication purposes
        })
    except Exception as e:
        # Handle potential DynamoDB errors
        print(f"Error storing user information: {e}")
        return False

    return True
