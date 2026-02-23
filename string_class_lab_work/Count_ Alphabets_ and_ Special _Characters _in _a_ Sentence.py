# Program to count the number of alphabets and special characters in a sentence

# Taking input from the user
sentence = input("Enter a sentence: ")

# -------------------------------
# Counting the number of alphabets
# -------------------------------
alpha_count = 0

for ch in sentence:
    # Check if the character is an alphabet (A–Z or a–z)
    if ch.isalpha():
        alpha_count += 1

print("Total number of alphabets:", alpha_count)


# --------------------------------------
# Counting the number of special characters
# --------------------------------------
special_count = 0

for ch in sentence:
    # If the character is NOT alphanumeric (not letter or digit),
    # then it is considered a special character (including spaces)
    if not ch.isalnum():
        special_count += 1

print("Total number of special characters:", special_count)

#output
#Enter a sentence: Hello World! 123
#Total number of alphabets: 10
#Total number of special characters: 3
