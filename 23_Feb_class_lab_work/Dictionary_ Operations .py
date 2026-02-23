# ------------------------------------------
# Program to demonstrate dictionary operations
# ------------------------------------------

# Create an empty dictionary
student = {}

# ------------------------------------------
# Inserting elements into the dictionary
# ------------------------------------------
student['name'] = 'Aviral'
student['roll'] = 43
student['age'] = 23

# Display the dictionary after insertion
print("Dictionary after initial insertion:")
print(student)

# ------------------------------------------
# Adding a new key-value pair
# Updating an existing key ('roll')
# ------------------------------------------
student["english"] = 89     # Adding new subject marks
student["roll"] = 1024      # Updating roll number

print("\nDictionary after adding and updating values:")
print(student)

# ------------------------------------------
# Displaying dictionary elements using loop
# ------------------------------------------
print("\nDisplaying key-value pairs:")
for key in student:
    print("Key:", key, " Value:", student[key])

#output
#Dictionary after initial insertion:
#{'name': 'Aviral', 'roll': 43, 'age': 23}

#Dictionary after adding and updating values:
#{'name': 'Aviral', 'roll': 1024, 'age': 23, 'english': 89}

#Displaying key-value pairs:
#Key: name  Value: Aviral
#Key: roll  Value: 1024
#Key: age  Value: 23
#Key: english  Value: 89
