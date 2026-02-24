# Program to check whether string contains only digits

text = input("Enter a string: ")            # Take string input

if text.isdigit():                          # Check if string contains only digits
    print("String contains only digits")    # Display result
else:                                       # Otherwise
    print("String does not contain only digits")  # Display result

# Output Example
# Enter a string: 12345
# String contains only digits
