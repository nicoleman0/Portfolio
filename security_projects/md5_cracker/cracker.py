import hashlib

def crack_hash(hash_value):
    """function that cracks a hashed password"""
    try:
        passFile = open("wordlist.txt", "r")
    except:
        print("No file found")
        quit()

    for password in passFile:
        encPass = password.encode("utf-8") 
        digest = hashlib.md5(encPass.strip()).hexdigest() 
        if digest == hash_value: 
            print("Password Found: " + password)

# using the function
if __name__ == "__main__":
    crack_hash("0192023a7bbd73250516f069df18b500") # this is "admin123" hashed using md5