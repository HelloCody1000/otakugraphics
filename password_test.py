from passwordHash import hash_password
from reviewPassword import check_password

# Test password
test_password = "MySecretPassword"

# Hash the password
hashed_password = hash_password(test_password)
print("Hashed Password:", hashed_password)

# Verify the password
is_correct = check_password(hashed_password, test_password)
print("Password is correct:", is_correct)

# Verify with a wrong password
is_correct = check_password(hashed_password, "WrongPassword")
print("Password is correct with wrong password:", is_correct)
