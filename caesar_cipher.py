import string

def caesar_encrypt(message, key):

    shift = key % 26 
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]) # Create a translation table

    encrypted_message = message.lower().translate(cipher) 
    return encrypted_message

def caesar_decrypt(encrypted_message, key):

    shift = 26 - (key % 26) # Calculate the shift for decryption
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    message = encrypted_message.translate(cipher)
    return message

message = 'Nick is the coolest person in the world'
key = 3

encrypted_message = caesar_encrypt(message, key) 
print(f"Encrypted message: {encrypted_message}")

decrypted_message = caesar_decrypt(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")