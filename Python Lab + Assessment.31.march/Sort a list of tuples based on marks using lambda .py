# Input: List of tuples (name, marks)
students = [
    ("Aman", 85),
    ("Riya", 92),
    ("Karan", 78),
    ("Neha", 88)
]

# Sorting based on marks (second element of tuple)
sorted_students = sorted(students, key=lambda x: x[1])

# Output
print("Sorted list (ascending by marks):")
print(sorted_students)

# If you want descending order
sorted_students_desc = sorted(students, key=lambda x: x[1], reverse=True)

print("\nSorted list (descending by marks):")
print(sorted_students_desc)

#output
#Sorted list (ascending by marks):
#[('Karan', 78), ('Aman', 85), ('Neha', 88), ('Riya', 92)]

#Sorted list (descending by marks):
#[('Riya', 92), ('Neha', 88), ('Aman', 85), ('Karan', 78)]
