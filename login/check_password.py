# check_password.py

import bcrypt

def check_password(stored_password_hash, plain_text_password):
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), stored_password_hash)
