# University Admission Eligibility Program

# Taking input
percentage = float(input("Enter 12th percentage: "))
maths = input("Did you study Mathematics? (yes/no): ").lower()
entrance_score = float(input("Enter entrance exam score: "))

# Checking eligibility conditions one by one
if percentage < 75:
    print("Not Eligible: Minimum 75% required in 12th grade.")

elif maths != "yes":
    print("Not Eligible: Mathematics is mandatory.")

elif entrance_score < 80:
    print("Not Eligible: Entrance exam score must be at least 80.")

else:
    print("Congratulations! You are Eligible for Admission.")
