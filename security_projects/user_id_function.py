def create_user(user_id, id_number, device_id, job):
    """Creates a user dictionary."""
    return {
        "user_id": user_id,
        "id_number": id_number,
        "device_id": device_id,
        "job": job
    }

# create the users
user_1 = create_user("nicoleman", "948201", "A923N09", "security analyst")
user_2 = create_user("lodeman", "493210", "A924N09", "security engineer")

# store in a list
users = [user_1, user_2]

# directly add to the list
users.append(create_user("brhunter", "084583", "B123C01", "developer"))

# Printing example
for user in users:
  print(user)

