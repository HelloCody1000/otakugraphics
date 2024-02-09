import boto3
import uuid
from botocore.exceptions import ClientError

# Assuming you have a function to generate a secure token
def generate_reset_token():
    return str(uuid.uuid4())

def send_password_reset_email(email):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('PasswordResetTokens')
    
    # Generate a unique token for password reset
    reset_token = generate_reset_token()
    
    # Store the token in DynamoDB with an expiration time
    response = table.put_item(
        Item={
            'email': email,
            'reset_token': reset_token,
            'expiration_time': int(time.time()) + 3600 # 1 hour from now
        }
    )
    
    # Send an email with the reset token link (use AWS SES or another email service)
    ses_client = boto3.client('ses', region_name='your-region')
    reset_link = f"https://yourdomain.com/reset_password?token={reset_token}"

    try:
        response = ses_client.send_email(
            Source='your-email@example.com',
            Destination={'ToAddresses': [email]},
            Message={
                'Subject': {'Data': 'Password Reset Link'},
                'Body': {
                    'Html': {'Data': f'<p>Please click on the link to reset your password: <a href="{reset_link}">Reset Password</a></p>'}
                }
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:", response['MessageId'])
