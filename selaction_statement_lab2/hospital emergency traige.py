# Hospital Emergency Triage System

# Taking input
age = int(input("Enter patient age: "))
heart_rate_abnormal = input("Is heart rate abnormal? (yes/no): ").lower()
severe_injury = input("Is there severe injury? (yes/no): ").lower()

# Categorizing patient condition
if heart_rate_abnormal == "yes" or severe_injury == "yes":
    category = "Critical"

else:
    category = "Moderate"

# Upgrade priority if age > 65 and condition is moderate
if age > 65 and category == "Moderate":
    category = "Critical (Upgraded due to Age)"

# Display category
print("Patient Category:", category)
