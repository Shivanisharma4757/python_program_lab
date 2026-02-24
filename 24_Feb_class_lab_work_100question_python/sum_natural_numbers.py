# Program to find the sum of first N natural numbers

n = int(input("Enter value of N: "))   # Take value of N from user
total = 0                              # Initialize sum variable

for i in range(1, n + 1):              # Loop from 1 to N
    total = total + i                  # Add current number to total

print("Sum of natural numbers:", total) # Display the sum

# Output Example
# Enter value of N: 5
# Sum of natural numbers: 15
