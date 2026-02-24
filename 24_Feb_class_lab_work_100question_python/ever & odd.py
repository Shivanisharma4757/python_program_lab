# Problem 8
# Program to check whether a number is even or odd without using modulus operator

# Taking input from the user
num = int(input("Enter a number: "))

# Checking even or odd without using %
# If a number divided by 2 and multiplied back by 2 gives the same number,
# then it is even; otherwise, it is odd.
if (num // 2) * 2 == num:
    print("The number is Even")
else:
    print("The number is Odd")

#output
#Enter a number: 5
#The number is Odd
