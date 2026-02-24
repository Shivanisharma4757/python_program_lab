# Program to rotate a list by K positions

numbers = [1, 2, 3, 4, 5]                 # Create a list of numbers
k = int(input("Enter number of rotations: "))  # Take number of rotations from user

n = len(numbers)                          # Find length of list
k = k % n                                 # Handle rotation greater than list size

rotated = numbers[k:] + numbers[:k]       # Rotate list using slicing

print("Rotated list:", rotated)           # Display rotated list

# Output Example
# Enter number of rotations: 2
# Rotated list: [3, 4, 5, 1, 2]
