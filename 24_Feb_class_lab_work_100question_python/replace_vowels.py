# Program to replace all vowels with *

text = input("Enter a string: ")            # Take string input from user

vowels = "aeiouAEIOU"                       # Define vowels

result = ""                                 # Variable to store modified string

for char in text:                           # Loop through each character in string
    if char in vowels:                      # Check if character is a vowel
        result += "*"                       # Replace vowel with *
    else:                                   # Otherwise
        result += char                      # Keep character as it is

print("Modified string:", result)           # Display result

# Output Example
# Enter a string: education
# Modified string: *d*c*t**n
