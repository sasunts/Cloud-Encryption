from cryptography.fernet import Fernet
import io

def keyGen():
    key = Fernet.generate_key()
    file = open('Keys/key.key', 'wb')
    file.write(key)
    file.close()

def keyRead():
    file = open('Keys/key.key', 'rb')
    key = file.read()
    file.close()
    return key

def encrypt(fileName, Key):
    with open("Files/"+ fileName, "rb") as f:
        data = f.read()
    fernet = Fernet(Key)
    encrypted = fernet.encrypt(data)
    with open("Files/"+ fileName, "wb") as f:
        f.write(encrypted)

def decrypt(fileName, Key):
    with open("Downloads/"+ fileName, "rb") as f:
        data = f.read()
    fernet = Fernet(Key)
    decrypted = fernet.decrypt(data)
    with open("Downloads/"+ fileName, "wb") as f:
        f.write(decrypted)