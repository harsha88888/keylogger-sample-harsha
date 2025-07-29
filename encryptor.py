from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt(data, key):
    return Fernet(key).encrypt(data.encode())

def decrypt(token, key):
    return Fernet(key).decrypt(token).decode()
