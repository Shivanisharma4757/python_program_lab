# Program to swap two numbers

# Take first number as input from user
num1 = float(input("Enter first number: "))

# Take second number as input from user
num2 = float(input("Enter second number: "))

# Display numbers before swapping
print("Before swapping:")
print("First number =", num1)
print("Second number =", num2)

# Swapping the numbers using a temporary variable
temp = num1      # Store num1 in temp
num1 = num2      # Assign num2 to num1
num2 = temp      # Assign temp (original num1) to num2

# Display numbers after swapping
print("After swapping:")
print("First number =", num1)
print("Second number =", num2)

# output
# Enter first number: 10
# Enter second number: 20
# Before swapping:
# First number = 10.0
# Second number = 20.0
# After swapping:
# First number = 20.0
# Second number = 10.0
