import os
import sys
from Crypto import Random
from Crypto.Cipher import AES
import os.path
from os import listdir
from os.path import isfile, join
import time
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage



def external(request):
    file = request.FILES['file']
    print("File is ", file)
    fs = FileSystemStorage()
    filename = fs.save(file.name, file)
    fileurl = fs.open(filename)
    templateurl = fs.url(filename)
    print("file raw url", filename)
    print("file full url", fileurl)
    print("template url", templateurl)
    global val

    # file_name = run([sys.executable,"D:\afs frontend\authsysproject\users\Script.py",fileurl,],shell=False,stdout=PIPE)

    data = {
        'h2': 'Your File Uploaded Successfully..!'}
    # print(file_name.stdout)

    return render(request, 'users/profile.html', data)


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

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(file_name)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)


key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('cls')


def submits(request):
    file_fullpath = sys.argv[0]
    file_name = sys.argv[1:]
    ok1=val()
    if request.POST.get('enc'):
        enc.encrypt_file(str('ok1'))
        data1 = {
            'h3': 'File Encrypted Successfully..!'
        }

    elif request.POST.get('dnc'):
        enc.decrypt_file(str('ok1'))
        data1 = {
            'h3': 'File Decrypted Successfully...!'
        }

    return render(request, 'users/profile.html', data1)


def home(request):
    return render(request, 'users/home.html')


def aboutus(request):
    return render(request, 'users/aboutus.html')


def homes(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')
