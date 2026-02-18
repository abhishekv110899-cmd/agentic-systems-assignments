# part2_contact_book.py

# Create dictionary

contacts = {"Ravi": "9876543210",
 "Anita": "9123456780",
 "Abhishek": "9920055667"}

# Print all contacts

print("All Contacts:")
for name, number in contacts.items():
    print(name, ":", number)

# Ask user for input
search_name = input("Enter name to search: ")

# Check if name exists
if search_name in contacts:
    print("Phone Number:", contacts[search_name])
else:
    print("Contact not found")