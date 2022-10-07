#!/usr/bin/python3
from Crypto.Util.number import (
    long_to_bytes as l2b,
    bytes_to_long as b2l,
    getPrime,
)

FLAG = b2l(b"t0o_sm4l1_effdc8")

p = getPrime(64)
q = getPrime(64)

e = 0x10001
n = p * q

ciphertext = pow(FLAG, e, n)

print(f"{e = :#x}")
print(f"{n = :#x}")
print(f"{ciphertext = :#x}")
