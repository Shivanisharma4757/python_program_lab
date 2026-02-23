# Number of rows and columns
n = 5

for i in range(n):
    for j in range(n):
        # Print star for borders
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print('*', end='')
        else:
            print(' ', end='')  # Hollow space
    print()  # Move to next row

#output

#*****
#*   *
#*   *
#*   *
#*****
