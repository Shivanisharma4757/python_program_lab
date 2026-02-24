# Program to count consonants in a string

text = input("Enter a string: ")            # Take string input

vowels = "aeiouAEIOU"                       # Define vowels

count = 0                                   # Variable to store consonant count

for char in text:                           # Loop through each character
    if char.isalpha() and char not in vowels:  # Check if character is consonant
        count += 1                          # Increase consonant count

print("Number of consonants:", count)       # Display consonant count

# Output Example
# Enter a string: hello
# Number of consonants: 3
