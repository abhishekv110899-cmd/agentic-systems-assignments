# part4_user_data_system.py

# Function to calculate average score
def calculate_average(users):
    averages = []
    for user in users:
        avg = sum(user["scores"]) / len(user["scores"])
        averages.append((user["name"], avg))
    return averages


# Function to check admin access
def has_admin_access(roles):
    return "admin" in roles


def main():
    # List of users (list of dictionaries)
    users = [
        {
            "name": "Alice",
            "scores": [80, 85, 90],
            "roles": {"admin", "editor"}
        },
        {
            "name": "Bob",
            "scores": [70, 75, 72],
            "roles": {"viewer"}
        }
    ]

    averages = calculate_average(users)

    for i, user in enumerate(users):
        print("\nName:", user["name"])
        print("Average Score:", averages[i][1])
        print("Admin Access:", has_admin_access(user["roles"]))


# Call main function
main()