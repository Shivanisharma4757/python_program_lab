# Program to count vowels in a string

text = input("Enter a string: ")            # Take string input

vowels = "aeiouAEIOU"                       # Define vowels

count = 0                                   # Variable to store vowel count

for char in text:                           # Loop through each character
    if char in vowels:                      # Check if character is vowel
        count += 1                          # Increase vowel count

print("Number of vowels:", count)           # Display vowel count

# Output Example
# Enter a string: hello world
# Number of vowels: 3
