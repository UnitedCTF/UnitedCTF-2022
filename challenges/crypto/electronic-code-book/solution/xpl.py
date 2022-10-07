#!/usr/bin/python3
from base64 import b64encode, b64decode
from string import hexdigits
from pwn import *

CHARSET = "".join(set("FLAG-" + hexdigits))
RHOST, RPORT = "nc.ctf.unitedctf.ca", 3000


def oracle(username: str) -> bytes:
    r.sendlineafter(b"> ", b"2")
    r.sendlineafter(b"Username: ", username.encode())
    r.recvuntil(b": ")
    return b64decode(r.recvline().decode().strip())


# 1st flag
r = remote(RHOST, RPORT)
cipher = oracle("A" * 16 + "admin")
token = b64encode(cipher[16:])
r.sendlineafter(b"> ", b"1")
r.sendlineafter(b": ", b"admin")
r.sendlineafter(b": ", token)
r.recvuntil(b": ")
r.success(r.recvline().decode().strip())

# 2nd flag
r = remote(RHOST, RPORT)
length = len(oracle(""))

flag = ""
for size in range(length - 1, -1, -1):
    baseline = oracle("A" * size)[:length]

    for c in CHARSET:
        ciphertext = oracle("A" * size + flag + c)[:length]
        if ciphertext == baseline:
            flag += c
            break
r.success(flag)
