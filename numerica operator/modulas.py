# Program to find modulus of numbers sequentially

numbers = input("Enter numbers for modulus operation (comma-separated): ")
num_list = [float(n) for n in numbers.split(',')]

result = num_list[0]
for n in num_list[1:]:
    if n == 0:
        print("Error: Cannot perform modulus by zero. Skipping.")
        continue
    result %= n

print("Final modulus result:", result)