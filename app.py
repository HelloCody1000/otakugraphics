from flask import Flask, request, jsonify
import boto3
from passwordHash import hash_password
#BackEnd communication
app = Flask(__name__)

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserCred')

@app.route('/create_user', methods=['POST'])
def create_user():
    # Extract data from the request
    data = request.json
    username = data['username']
    user_id = data['userid']
    password = data['password']
    email = data['email']

    # Hash the user ID, password, and email
    hashed_user_id = hash_password(user_id)
    hashed_password = hash_password(password)
    hashed_email = hash_password(email)

    # Store the data in DynamoDB
    response = table.put_item(
        Item={
            'username': username,
            'hashed_user_id': hashed_user_id,
            'hashed_password': hashed_password,
            'hashed_email': hashed_email
        }
    )

    return jsonify({'message': 'User information stored successfully.'})

if __name__ == '__main__':
    app.run(debug=True)
