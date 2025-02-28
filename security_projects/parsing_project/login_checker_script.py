with open("company_users.txt", "r") as file:
    file_text = file.read()
usernames = file_text.split("\n")

def login_checker(login_list, current_user):
    counter = 0
    for i in login_list:
        if i == current_user:
            counter += 1
    if counter >= 5:
        return "You have attempted to login too many times."
    else:
        return "Login successful."
