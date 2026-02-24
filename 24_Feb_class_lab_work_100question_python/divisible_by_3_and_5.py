# Check whether a number is divisible by both 3 and 5

num = int(input())  # Take number input from user

if num % 3 == 0 and num % 5 == 0:  # Check if number divisible by 3 and 5
    print("Divisible by 3 and 5")  # Print if condition is true
else:
    print("Not Divisible by 3 and 5")  # Print if condition is false


# Output:
# Input: 15
# Output: Divisible by 3 and 5
