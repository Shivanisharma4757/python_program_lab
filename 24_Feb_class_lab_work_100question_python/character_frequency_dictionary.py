# Program to count character frequency using dictionary

text = input("Enter a string: ")        # Take string input from user

freq = {}                               # Create empty dictionary for frequency

for char in text:                       # Loop through each character in string
    if char in freq:                    # Check if character already exists in dictionary
        freq[char] = freq[char] + 1     # Increase frequency count
    else:                               # Otherwise
        freq[char] = 1                  # Initialize frequency

print("Character frequency:", freq)     # Display frequency dictionary

# Output Example
# Enter a string: hello
# Character frequency: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
