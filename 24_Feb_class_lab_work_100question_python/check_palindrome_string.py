# Program to check whether a string is palindrome

text = input("Enter a string: ")        # Take string input from user

reversed_text = text[::-1]              # Reverse the string using slicing

if text == reversed_text:               # Compare original string with reversed string
    print("String is palindrome")       # Display message if palindrome
else:                                   # Otherwise
    print("String is not palindrome")   # Display message if not palindrome

# Output Example
# Enter a string: madam
# String is palindrome
