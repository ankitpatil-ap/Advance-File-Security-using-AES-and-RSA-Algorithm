import sys
from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time
#from PIL import Image

from django.shortcuts import render

file_fullpath = sys.argv[0]
file_name = sys.argv[1:]

file = open(str(file_fullpath))
print(file)
def submits(request):
    global data1
    if request.POST.get('enc'):
        enc.encrypt_file(file)
        data1 = {
            'h3': 'File Encrypted Successfully..!'
        }

    elif request.POST.get('dnc'):
        enc.decrypt_file(file)
        data1 = {
            'h3': 'File Decrypted Successfully...!'
        }

    return render(request, 'users/profile.html', data1)

class Encryptor:
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file):
        with open(file, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(file)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file):
        with open(file, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file)


key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('cls')



