# Program to generate Fibonacci series using while loop

n = int(input("Enter number of terms: "))  # Take number of terms from user
a = 0                                      # First Fibonacci number
b = 1                                      # Second Fibonacci number
count = 0                                  # Counter variable

while count < n:                           # Loop runs until count reaches n
    print(a)                               # Print current Fibonacci number
    c = a + b                              # Calculate next number
    a = b                                  # Update first number
    b = c                                  # Update second number
    count = count + 1                      # Increase counter

# Output Example
# Enter number of terms: 5
# 0
# 1
# 1
# 2
# 3
