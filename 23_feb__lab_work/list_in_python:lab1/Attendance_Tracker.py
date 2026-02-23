# Program Name: Attendance Tracker

attendance = [1,0,1,1,0,0,1,1,1,0]

percentage = (sum(attendance) / len(attendance)) * 100

print("Attendance %:", percentage)

if percentage < 75:
    print("Below 75% - Warning")

# Replace consecutive absences
for i in range(len(attendance)-1):
    if attendance[i] == 0 and attendance[i+1] == 0:
        attendance[i] = "Warning"

print("Updated Attendance:", attendance)

# Output:
# Attendance %: 60.0
# Below 75% - Warning
# Updated Attendance: [1, 0, 1, 1, 'Warning', 0, 1, 1, 1, 0]
