# Program to count vowels in a string using a loop

# Take input from the user
text = input("Enter a string: ")

# Initialize vowel counter
count = 0

# Convert string to lowercase to check both uppercase and lowercase vowels
text = text.lower()

# Loop through each character in the string
for char in text:
    
    # Check if the character is a vowel
    if char in ('a', 'e', 'i', 'o', 'u'):
        count += 1   # Increase count if vowel is found

# Display the result
print("Number of vowels in the string:", count)
#output
#Enter a string: Hello Python World
#Number of vowels in the string: 4
