#!/usr/bin/python3
from Crypto.Util.number import (
    long_to_bytes as l2b,
    bytes_to_long as b2l,
    getPrime,
    isPrime,
)

FLAG = b2l(b"FLAG-c4r3ful_w1th_m4th_tr34t_1t_l1k3_m3th")

p = getPrime(2048)
q = p + 1
while not isPrime(q):
    q += 1

e = 0x10001
n = p * q

ciphertext = pow(FLAG, e, n)

print(f"{e = :#x}")
print(f"{n = :#x}")
print(f"{ciphertext = :#x}")
