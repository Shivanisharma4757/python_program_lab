# Program to reverse a string using for loop

text = input("Enter a string: ")           # Take string input from user
reverse = ""                               # Initialize empty string for reversed result

for char in text:                          # Loop through each character
    reverse = char + reverse               # Add character at the beginning of reverse string

print("Reversed string:", reverse)         # Display reversed string

# Output Example
# Enter a string: python
# Reversed string: nohtyp
