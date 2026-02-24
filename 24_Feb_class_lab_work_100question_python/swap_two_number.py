# Read two numbers from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Display original values
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swapping without using third variable
a = a + b
b = a - b
a = a - b

# Display swapped values
print("After swapping:")
print("a =", a)
print("b =", b)

#output
#Enter first number: 10
#Enter second number: 20
#Before swapping:
#a = 10
#b = 20
#After swapping:
#a = 20
#b = 10
