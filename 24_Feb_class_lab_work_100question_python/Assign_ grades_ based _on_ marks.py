# Problem 12
# Program to assign grades based on marks

# Taking input from the user
marks = float(input("Enter the marks: "))

# Assigning grade based on marks
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

# Printing the result
print("Grade:", grade)

#output
#Enter the marks: 78
#Grade: B
