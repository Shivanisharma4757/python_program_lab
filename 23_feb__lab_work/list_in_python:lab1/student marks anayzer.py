# List of student marks (can include invalid marks)
marks = [95, 85, 102, -5, 76, 88, 90, 67, 110]

# 1️ Remove invalid marks (less than 0 or greater than 100)
valid_marks = [m for m in marks if 0 <= m <= 100]

# 2️ Calculate average
average = sum(valid_marks) / len(valid_marks)

# 3️ Find topper(s)
max_mark = max(valid_marks)
toppers = [i+1 for i, m in enumerate(valid_marks) if m == max_mark]  # student numbers (1-based)

# 4️ Display grade based on average
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display results
print("Valid marks:", valid_marks)
print(f"Average marks: {average:.2f}")
print(f"Topper(s) student number(s): {toppers} with marks {max_mark}")
print(f"Grade based on average: {grade}")

# output
# Valid marks: [95, 85, 76, 88, 90, 67]
# Average marks: 83.50
# Topper(s) student number(s): [1] with marks 95
# Grade based on average: B
