# ------------------------------------------
# Program to find union of two sets
# ------------------------------------------

# Creating first set
set1 = {45, 67, 89, 34, 78}
print("First set :", set1)

print("------------------------------------")

# Creating second set
set2 = {23, 56, 89, 90, 34}
print("Second set :", set2)

print("------------------------------------")

# Finding union of two sets
set3 = set1.union(set2)

print("Union of set1 and set2 is :", set3)

#output
#First set : {34, 67, 45, 78, 89}
#------------------------------------
#Second set : {34, 23, 56, 89, 90}
#------------------------------------
#Union of set1 and set2 is : {34, 67, 45, 78, 89, 23, 56, 90}
