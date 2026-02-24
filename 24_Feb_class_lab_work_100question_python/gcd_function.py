# Program to find GCD using a function

def find_gcd(a, b):                       # Define function to find GCD
    while b != 0:                         # Loop until b becomes 0
        temp = b                          # Store value of b
        b = a % b                         # Update b with remainder
        a = temp                          # Update a with previous b
    return a                              # Return GCD


x = int(input("Enter first number: "))    # Take first number from user
y = int(input("Enter second number: "))   # Take second number from user

result = find_gcd(x, y)                   # Call GCD function

print("GCD is:", result)                  # Display GCD

# Output Example
# Enter first number: 12
# Enter second number: 18
# GCD is: 6
