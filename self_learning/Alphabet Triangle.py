# Number of rows
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end='')  # 65 is ASCII of 'A'
    print()  # Move to next line

output
A
AB
ABC
ABCD
ABCDE
