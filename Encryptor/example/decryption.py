import os
from cryptography.fernet import Fernet
path = r'C:\Users\User\PycharmProjects\encryptor\example'


with open("encryptionkey.txt","rb") as key:
    decryptionkey = key.read()

print(os.listdir(path))
for file in os.listdir(path):
    if file == 'encryptionkey.txt':
        continue
    elif file == 'encryptorscript.py':
        continue
    elif file == 'decryption.py':
        continue
    with open(file, 'rb') as targetfile:
        contents = targetfile.read()
    decrypted_data = Fernet(decryptionkey).decrypt(contents)
    with open(file, 'wb') as encrypted_file:
        encrypted_file.write(decrypted_data)