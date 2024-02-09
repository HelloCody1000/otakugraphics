import boto3

# Assuming authenticate_user and store_user_info functions are defined in their respective files
from login.authenticate_user import authenticate_user
from store_user_info import store_user_info

def is_valid_username_password(username, password):
    # Add your logic to check if the username and password meet the criteria
    # (e.g., at least one capital letter, one number, and one special character)
    return True

def is_username_available(username):
    # Check in DynamoDB if the username is available
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')
    response = table.get_item(Key={'username': username})
    return 'Item' not in response

def main():
    choice = input("Choose an option: \n1. Login \n2. Create Account\n")

    if choice == '1':
        # Login flow
        username = input("Enter username: ")
        user_id = input("Enter user ID: ")
        password = input("Enter password: ")
        success, message = authenticate_user(username, user_id, password)
        print(message)

    elif choice == '2':
        # Create Account flow
        while True:
            username = input("Choose a username: ")
            if not is_username_available(username):
                print("Username taken. Please choose a different username.")
                continue

            user_id = input("Set your user ID: ")
            password = input("Set your password: ")

            if not is_valid_username_password(username, password):
                print("Invalid username or password. Ensure it meets the criteria.")
                continue

            # Assuming the store_user_info function takes username, user_id, and password as arguments
            store_user_info(username, user_id, password)
            print("Account created successfully.")
            break

    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()
