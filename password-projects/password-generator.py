import random
import string

def generate_password(length: int = 10):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length)) # generate a random password
    return password

password = generate_password()
print (f"Generated password: {password}")