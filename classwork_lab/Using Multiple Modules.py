# Python Program: Using Multiple Modules

# ----------------------------
# Import Modules
# ----------------------------
import math        # For mathematical operations
import random      # For generating random numbers
import datetime    # For date and time operations

# ----------------------------
# Math Module Example
# ----------------------------
print("Math Module Examples:")
num = 16
print(f"Square root of {num} is {math.sqrt(num)}")
angle = math.pi / 4  # 45 degrees in radians
print(f"Cosine of 45 degrees: {math.cos(angle):.2f}")
print(f"Factorial of 5: {math.factorial(5)}\n")

# ----------------------------
# Random Module Example
# ----------------------------
print("Random Module Examples:")
print("Random integer between 1 and 10:", random.randint(1, 10))
print("Random choice from list [10, 20, 30, 40]:", random.choice([10, 20, 30, 40]))
print("Random float between 0 and 1:", random.random(), "\n")

# ----------------------------
# Datetime Module Example
# ----------------------------
print("Datetime Module Examples:")
now = datetime.datetime.now()  # Current date and time
print("Current date and time:", now)
print("Current year:", now.year)
print("Current month:", now.month)
print("Current day:", now.day)

output

Math Module Examples:
Square root of 16 is 4.0
Cosine of 45 degrees: 0.71
Factorial of 5: 120

Random Module Examples:
Random integer between 1 and 10: 7
Random choice from list [10, 20, 30, 40]: 20
Random float between 0 and 1: 0.5321461275

Datetime Module Examples:
Current date and time: 2026-02-22 14:35:10.123456
Current year: 2026
Current month: 2
Current day: 22
