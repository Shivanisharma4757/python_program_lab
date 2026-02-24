# Program to calculate power without using exponent operator

base = int(input("Enter base: "))          # Take base value from user
exp = int(input("Enter exponent: "))       # Take exponent value from user

result = 1                                 # Initialize result variable

for i in range(exp):                       # Loop runs exponent times
    result = result * base                 # Multiply base repeatedly

print("Result:", result)                   # Display the power result

# Output Example
# Enter base: 2
# Enter exponent: 4
# Result: 16
