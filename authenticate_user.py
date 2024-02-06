import boto3
from passwordHash import hash_password
from reviewPassword import check_password

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def authenticate_user(username, user_id, password):
    # Retrieve user data from DynamoDB
    try:
        response = table.get_item(Key={'username': username})
        user_data = response.get('Item', None)
        if not user_data:
            return False, "User not found."

        # Extract stored hashed user ID and password
        stored_hashed_user_id = user_data['hashed_user_id']
        stored_hashed_password = user_data['hashed_password']

        # Check if the provided user ID and password match the stored ones
        if check_password(stored_hashed_user_id, user_id) and check_password(stored_hashed_password, password):
            return True, "Authentication successful."
        else:
            return False, "Invalid user ID or password."

    except Exception as e:
        return False, f"Error during authentication: {e}"

# Example usage
username = input("Enter your username: ")
user_id = input("Enter your user ID: ")
password = input("Enter your password: ")

is_authenticated, message = authenticate_user(username, user_id, password)
print(message)
