# part3_employee_roles.py

# Employee tuple
employee = (101, "Ayush", "IT")

# Roles set
roles = {"admin", "editor", "viewer"}

# Print employee info using indexing
print("Employee ID:", employee[0])
print("Employee Name:", employee[1])
print("Department:", employee[2])

# Check admin access
if "editor" in roles:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")