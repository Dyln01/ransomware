import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# You can change this to a hard drive or other folder. Include the path or it needs to be in the same directory
folder_name = "cryptme"

# Key that the file are encrypted with in bottom of terminal or a text file
key = b'\xed\x1a\x00\xee\x11\xacd\xe8\x06H\x07s\x8c\xb9\xc65)\xbbd\xeb\x16\xb7\x18t\x18\x1b*q\x16\x1eU\xf3'
# IV that the files are encrypted with in bottom of terminal or a text file
iv = b'\x8e\xc0\x81\x1d\xdc\x8b\x89\xf0\xcc\x04\x91\xa3\xcc\xb0J~'

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

def decrypt(file_path, ciphertext):
    decryptor = cipher.decryptor()
    decrypted_padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(decrypted_padded_plaintext) + unpadder.finalize()

    new_file_path = file_path
    with open(new_file_path, "wb") as file:
        file.write(plaintext)
        

def isFolder(file_path):
    for file_name in os.listdir(file_path):
            file_path_dir = os.path.join(file_path, file_name)
            is_folder = os.path.isdir(file_path_dir)
            
            if is_folder == True:
                isFolder(file_path_dir)
            else:
                with open(file_path_dir, "rb") as file:
                    ciphertext = file.read()
                
                decrypt(file_path_dir, ciphertext)
                

for file_name in os.listdir(folder_name):
    
    file_path = os.path.join(folder_name, file_name)

    if os.path.isdir(file_path):
        for file_name_dir in os.listdir(file_path):
            file_path_dir = os.path.join(file_path, file_name_dir)
            is_folder = os.path.isdir(file_path_dir)
            
            if is_folder == True:
                isFolder(file_path_dir)
            else:
                with open(file_path_dir, "rb") as file:
                    ciphertext = file.read()
                
                decrypt(file_path_dir,ciphertext)
                
    else:
        with open(file_path, "rb") as file:
            ciphertext = file.read()
            
        decrypt(file_path, ciphertext)
        
print('Successfully decrypted your files...')