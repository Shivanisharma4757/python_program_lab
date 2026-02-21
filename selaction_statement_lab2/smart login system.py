# Smart Login System Program

# Predefined username and password
correct_username = "admin"
correct_password = "1234"

attempts = 0  # Counter for failed attempts

# Allow maximum 3 attempts
while attempts < 3:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # Validate username and password
    if username == correct_username and password == correct_password:
        print("Login Successful!")
        break
    else:
        attempts += 1
        print("Invalid Username or Password.")
        print("Attempts left:", 3 - attempts)

# Lock account after 3 failed attempts
if attempts == 3:
    print("Account Locked due to 3 failed attempts.")
