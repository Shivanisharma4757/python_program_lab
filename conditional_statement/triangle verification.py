# Program to check triangle validity and classify by sides and angle

# Taking input for sides
a_input = input("Enter side a: ")
b_input = input("Enter side b: ")
c_input = input("Enter side c: ")

# Validation: Check if inputs are numeric
if a_input.replace('.', '', 1).isdigit() and b_input.replace('.', '', 1).isdigit() and c_input.replace('.', '', 1).isdigit():
    
    a = float(a_input)
    b = float(b_input)
    c = float(c_input)
    
    # Check if sides are positive
    if a > 0 and b > 0 and c > 0:
        
        # Triangle inequality check
        if (a + b > c) and (a + c > b) and (b + c > a):
            print("\nThe sides CAN form a triangle.")
            
            # --- Classification by sides ---
            if a == b == c:
                side_type = "Equilateral"
            elif a == b or b == c or a == c:
                side_type = "Isosceles"
            else:
                side_type = "Scalene"
            
            print("Triangle Type by Sides:", side_type)
            
            # --- Classification by angles using Pythagoras (simple method) ---
            sides = sorted([a, b, c])  # Sort sides to identify largest side as hypotenuse
            if abs(sides[2]**2 - (sides[0]**2 + sides[1]**2)) < 1e-5:
                angle_type = "Right-Angled"
            elif sides[2]**2 < (sides[0]**2 + sides[1]**2):
                angle_type = "Acute-Angled"
            else:
                angle_type = "Obtuse-Angled"
            
            print("Triangle Type by Angles:", angle_type)
        
        else:
            print("\nThe sides CANNOT form a triangle.")
    
    else:
        print("Error: All sides must be greater than 0.")

else:
    print("Error: Please enter valid numeric values.")
