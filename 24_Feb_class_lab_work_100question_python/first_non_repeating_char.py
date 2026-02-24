# Program to find first non-repeating character in a string

text = input("Enter a string: ")            # Take string input

for char in text:                           # Loop through each character
    if text.count(char) == 1:               # Check if character appears only once
        print("First non-repeating character:", char)  # Display character
        break                               # Stop loop after finding first one

# Output Example
# Enter a string: swiss
# First non-repeating character: w
