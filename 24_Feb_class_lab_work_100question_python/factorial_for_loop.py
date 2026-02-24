# Program to find factorial using for loop

num = int(input("Enter a number: "))   # Take number input from user
fact = 1                               # Initialize factorial variable

for i in range(1, num + 1):            # Loop from 1 to the number
    fact = fact * i                    # Multiply factorial with current value

print("Factorial is:", fact)           # Display factorial result

# Output Example
# Enter a number: 5
# Factorial is: 120
