# Validate username and password

username = input("Enter username: ")  # Take username input
password = input("Enter password: ")  # Take password input

if username == "admin" and password == "1234":  # Check correct username and password
    print("Login Successful")  # Print if credentials are correct
else:
    print("Invalid Credentials")  # Print if credentials are wrong


# Output:
# Enter username: admin
# Enter password: 1234
# Login Successful
