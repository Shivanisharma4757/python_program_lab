# Program to check whether a string is palindrome using function

def check_palindrome(text):                 # Define function to check palindrome
    if text == text[::-1]:                  # Compare string with its reverse
        return True                         # Return True if palindrome
    else:                                   # Otherwise
        return False                        # Return False


string = input("Enter a string: ")          # Take string input from user

if check_palindrome(string):                # Call function
    print("Palindrome String")              # Display palindrome result
else:                                       # Otherwise
    print("Not a Palindrome")               # Display not palindrome


# Output Example
# Enter a string: madam
# Palindrome String
