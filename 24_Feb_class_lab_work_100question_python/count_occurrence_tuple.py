# Program to count occurrence of an element in a tuple

numbers = (1, 2, 3, 2, 4, 2, 5)       # Create a tuple with repeated elements

element = int(input("Enter element to count: "))   # Take element input from user

count = 0                             # Initialize counter

for num in numbers:                   # Loop through tuple elements
    if num == element:                # Check if element matches
        count = count + 1             # Increase counter

print("Occurrence of element:", count) # Display occurrence count

# Output Example
# Enter element to count: 2
# Occurrence of element: 3
