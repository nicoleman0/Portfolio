with open("company_users.txt", "r") as file:
    user_list = file.read()

remove_users = ["nicoleman", "elarson", "jadozer"]

user_list = user_list.split()

users_to_keep = []

for user in user_list:
    if user not in remove_users:
        users_to_keep.append(user)

# only prints if there are users to remove
if len(user_list) != len(users_to_keep):
    print(f"Removed users: {[user for user in user_list if user in remove_users]}")
else:
    print("There are no users to remove.")

# Convert the list back to a string with spaces between usernames
updated_user_list_str = " ".join(users_to_keep)

with open("company_users.txt", "w") as file:
    file.write(updated_user_list_str)