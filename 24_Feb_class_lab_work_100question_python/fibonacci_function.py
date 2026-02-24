# Program to generate Fibonacci series using a function

def fibonacci(n):                          # Define function to generate Fibonacci series
    a = 0                                  # First Fibonacci number
    b = 1                                  # Second Fibonacci number
    
    for i in range(n):                     # Loop runs n times
        print(a)                           # Print current Fibonacci number
        c = a + b                          # Calculate next Fibonacci number
        a = b                              # Update first number
        b = c                              # Update second number


terms = int(input("Enter number of terms: "))  # Take number of terms from user

fibonacci(terms)                          # Call Fibonacci function

# Output Example
# Enter number of terms: 6
# 0
# 1
# 1
# 2
# 3
# 5
