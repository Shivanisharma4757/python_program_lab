# Program to remove a key from dictionary safely

data = {"a": 1, "b": 2, "c": 3, "d": 4}     # Create dictionary

key = input("Enter key to remove: ")        # Take key input from user

if key in data:                             # Check if key exists in dictionary
    del data[key]                           # Delete the key from dictionary
    print("Updated dictionary:", data)      # Display updated dictionary
else:                                       # Otherwise
    print("Key not found")                  # Display message if key not present

# Output Example
# Enter key to remove: b
# Updated dictionary: {'a': 1, 'c': 3, 'd': 4}
