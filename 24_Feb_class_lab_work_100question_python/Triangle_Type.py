# Determine type of triangle

a = int(input("Enter side 1: "))  # Take first side input
b = int(input("Enter side 2: "))  # Take second side input
c = int(input("Enter side 3: "))  # Take third side input

if a == b and b == c:  # Check if all sides are equal
    print("Equilateral Triangle")  # All sides equal
elif a == b or b == c or a == c:  # Check if any two sides are equal
    print("Isosceles Triangle")  # Two sides equal
else:
    print("Scalene Triangle")  # All sides different


# Output:
# Enter side 1: 5
# Enter side 2: 5
# Enter side 3: 5
# Equilateral Triangle

