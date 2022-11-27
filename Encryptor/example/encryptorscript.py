import os
from cryptography.fernet import Fernet
path = r'C:\Users\User\PycharmProjects\encryptor\example'


key = Fernet.generate_key()
with open(r'C:\Users\User\PycharmProjects\encryptor\example\encryptionkey.txt','wb') as keyfile:
        keyfile.write(key)

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
    encrypted_data = Fernet(key).encrypt(contents)
    with open(file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
