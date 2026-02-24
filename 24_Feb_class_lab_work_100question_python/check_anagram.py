# Program to check whether two strings are anagrams

str1 = input("Enter first string: ")      # Take first string input
str2 = input("Enter second string: ")     # Take second string input

if sorted(str1) == sorted(str2):          # Compare sorted characters of both strings
    print("Strings are anagrams")         # Display result if they are anagrams
else:                                     # Otherwise
    print("Strings are not anagrams")     # Display result if not anagrams

# Output Example
# Enter first string: listen
# Enter second string: silent
# Strings are anagrams
