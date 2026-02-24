# Program to find the greatest of four numbers

a = int(input("Enter first number: "))      # Taking first number input from user
b = int(input("Enter second number: "))     # Taking second number input from user
c = int(input("Enter third number: "))      # Taking third number input from user
d = int(input("Enter fourth number: "))     # Taking fourth number input from user

largest = a                                 # Assume first number is the largest initially

if b > largest:                             # Check if second number is greater than current largest
    largest = b                             # Update largest with second number

if c > largest:                             # Check if third number is greater than current largest
    largest = c                             # Update largest with third number

if d > largest:                             # Check if fourth number is greater than current largest
    largest = d                             # Update largest with fourth number

print("Greatest number is:", largest)       # Print the largest number

# Output Example
# Enter first number: 5
# Enter second number: 9
# Enter third number: 3
# Enter fourth number: 7
# Greatest number is: 9
