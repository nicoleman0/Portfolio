import hashlib
import getpass

password_managger = {}

def create_account():
    username = input("Enter your desired username: ")
    password = getpass.getpass("Now enter your desired password: ") # getpass hides the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_managger[username] = hashed_password # Store the hashed password in the dictionary
    print("Account has been created.")
        
    def login():
        username = input("Please enter your username: ")
        password = getpass.getpass("Now enter your password: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        # Check if the hashed password is in the dictionary
        if password_managger.get(username) == hashed_password: 
            print("Login successful.")
        else:
            print("Login failed.")
    
    def main():
        while True:
            choice = input("Enter 1 to create an account, 2 to login, or 0 to exit the program: ")
            if choice == "1":
                create_account()
            elif choice == "2":
                login()
            elif choice == "0":
                break
            else:
                print("Please enter a valid choice.")
    
    if __name__ == "__main__": # This is the entry point of the program
        main()