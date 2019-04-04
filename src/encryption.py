from cryptography.fernet import Fernet


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

#TODO