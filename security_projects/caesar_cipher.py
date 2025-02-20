import string

def caesar_encrypt(message, key):

    shift_amount = key % 26 
    # Create a translation table that maps each letter to its shifted counterpart
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift_amount:] + string.ascii_lowercase[:shift_amount])

    encrypted_message = message.lower().translate(cipher) 
    return encrypted_message

def caesar_decrypt(encrypted_message, key):

    shift_amount = 26 - (key % 26) # Calculate the shift for decryption
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift_amount:] + string.ascii_lowercase[:shift_amount])

    message = encrypted_message.translate(cipher)
    return message

message = 'Nick is the coolest person in the world'
key = 3

encrypted_message = caesar_encrypt(message, key) 
print(f"Encrypted message: {encrypted_message}")

decrypted_message = caesar_decrypt(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")
