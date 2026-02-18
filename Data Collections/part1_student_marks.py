# part1_student_marks.py

# Store marks of 8 students
marks = [78, 85, 90, 65, 88, 92, 80, 75]

# Print full list
print("All Marks:", marks)

# First 3 marks using slicing
print("First 3 marks:", marks[:3])

# Last 3 marks using slicing
print("Last 3 marks:", marks[-3:])

# Calculate highest, lowest, and average
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)