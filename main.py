# create encryption and decryption functions using AES


def encryption_function(key, plaintext):
    """create encryption function using AES"""
    # create a new AES cipher using the given key
    cipher = AES.new(key, AES.MODE_ECB)
    # encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext)
    # return the ciphertext
    return ciphertext

# create decryption function using AES
def decryption_function(key, ciphertext):
    """create decryption function using AES"""
    # create a new AES cipher using the given key
    cipher = AES.new(key, AES.MODE_ECB)
    # decrypt the ciphertext
    plaintext = cipher.decrypt(ciphertext)
    # return the plaintext
    return plaintext

# import the AES module
import AES
