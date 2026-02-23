# File: car_details.py

# Creating a dictionary named 'car'
# It contains:
# 1. brand → a string value
# 2. specs → a tuple containing fuel type, transmission type, and color
car = {
    "brand": "Toyota",
    "specs": ("Petrol", "Manual", "Red")
}

# Accessing and printing the value associated with the key "brand"
print("Car Brand:", car["brand"])

# Accessing and printing the tuple stored under the key "specs"
print("Specifications:", car["specs"])


# Output:
# Car Brand: Toyota
# Specifications: ('Petrol', 'Manual', 'Red')
