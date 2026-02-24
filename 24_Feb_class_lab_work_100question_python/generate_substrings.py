# Program to generate all substrings of a string

text = input("Enter a string: ")            # Take string input

length = len(text)                          # Find length of string

for i in range(length):                     # Loop for starting index
    for j in range(i + 1, length + 1):      # Loop for ending index
        print(text[i:j])                    # Print substring

# Output Example
# Enter a string: abc
# a
# ab
# abc
# b
# bc
# c
