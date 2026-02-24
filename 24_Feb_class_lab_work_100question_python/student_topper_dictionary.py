# Program to create a dictionary of student marks and find the topper

marks = {"Rahul": 85, "Amit": 92, "Neha": 88, "Riya": 95}   # Create dictionary with student names and marks

topper = ""                                                 # Variable to store topper name
highest = 0                                                 # Variable to store highest marks

for student in marks:                                       # Loop through dictionary keys
    if marks[student] > highest:                            # Check if marks are greater than current highest
        highest = marks[student]                             # Update highest marks
        topper = student                                     # Update topper name

print("Topper:", topper)                                     # Display topper name
print("Marks:", highest)                                     # Display highest marks

# Output Example
# Topper: Riya
# Marks: 95
