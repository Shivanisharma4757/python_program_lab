# Program to print a star pattern using for loop

rows = int(input("Enter number of rows: "))  # Take number of rows from user

for i in range(1, rows + 1):                 # Outer loop controls rows
    for j in range(i):                       # Inner loop prints stars
        print("*", end="")                   # Print star without new line
    print()                                  # Move to next line

# Output Example
# Enter number of rows: 5
# *
# **
# ***
# ****
# *****
