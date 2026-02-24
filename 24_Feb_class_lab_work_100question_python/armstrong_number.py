# Program to check whether a number is an Armstrong number

num = int(input("Enter a number: "))   # Take number input from user
temp = num                             # Store original number
sum = 0                                # Variable to store sum of cubes

while num > 0:                         # Loop runs while number is greater than 0
    digit = num % 10                   # Extract last digit
    sum = sum + digit**3               # Add cube of digit to sum
    num = num // 10                    # Remove last digit

if sum == temp:                        # Check if sum equals original number
    print("Armstrong Number")          # Display Armstrong result
else:                                  # Otherwise
    print("Not an Armstrong Number")   # Display not Armstrong

# Output Example
# Enter a number: 153
# Armstrong Number
