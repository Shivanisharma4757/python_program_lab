# Program to calculate factorial of a number using a for loop

# Take input from the user
num = int(input("Enter a number: "))

# Check if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers")

# Factorial of 0 is 1
elif num == 0:
    print("Factorial of 0 is 1")

else:
    factorial = 1  # Initialize factorial to 1
    
    # Multiply numbers from 1 to num
    for i in range(1, num + 1):
        factorial = factorial * i
    
    print("Factorial of", num, "is", factorial)
#output
#Enter a number: 5
#Factorial of 5 is 120
