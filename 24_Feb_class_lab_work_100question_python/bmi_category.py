# Calculate BMI category

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

# Calculating BMI
bmi = weight / (height ** 2)

# Checking BMI category
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal Weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

#output
#Enter weight (kg): 70
#Enter height (m): 1.75
#Normal Weight
