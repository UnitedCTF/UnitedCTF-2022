#!/usr/bin/python3
from pwn import *
import re

RHOST, RPORT = "nc.ctf.unitedctf.ca", 5000
REGEX = re.compile("^(-?\d+)\*x ([+-] \d+) = (-?\d+)$")

r = remote(RHOST, RPORT)
r.recvline()

for _ in range(100):
    equation = r.recvline().decode().split(":")[1].strip()
    match = REGEX.match(equation)
    a, b, c = (
        int(match.group(1)),
        int(match.group(2).replace(" ", "")),
        int(match.group(3)),
    )
    x = (c - b) // a
    r.sendlineafter(b"Answer: ", str(x).encode())

r.success(r.recvline().decode())
