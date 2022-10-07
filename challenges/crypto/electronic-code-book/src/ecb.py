#!/usr/bin/python3
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from base64 import b64encode
import os

FLAG1 = os.getenv("FLAG1")
FLAG2 = os.getenv("FLAG2")
KEY = get_random_bytes(16)


def encrypt(data: bytes, secret=FLAG2.encode(), key=KEY):
    aes = AES.new(key, AES.MODE_ECB)
    cipher = aes.encrypt(pad(data + secret, 16))
    return b64encode(cipher).decode()


USERNAME = "admin"
TOKEN = encrypt(USERNAME.encode())

BANNER = """\
~~~ Welcome to Secure Authenticator v1.0 🔒 ~~~
"""
MENU = """\
[1] Login
[2] Register
[0] Quit
"""

print(BANNER)
while True:
    print(MENU)
    choice = input("> ")
    if choice == "0":
        print("Good bye")
        exit(0)

    elif choice == "1":
        username = input("Username: ")
        token = input("Token: ")
        if username == USERNAME:
            if token == TOKEN:
                print(f"Welcome admin, here's your note: {FLAG1}")
                exit(0)
            print("Wrong token!")
        else:
            print(
                "Sorry, can't log you in! Forgot to store your credentials in the database."
            )

    elif choice == "2":
        username = input("Username: ")
        if username == USERNAME:
            print("You can't use this username.")
            continue
        token = encrypt(username.encode())
        print(f"Here's your token, use is to login: {token}")

    else:
        print("No such option.")
