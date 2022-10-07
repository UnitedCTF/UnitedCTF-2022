bits 64

%macro clear 1
	xor %1,%1
%endmacro

section .text alloc exec write align=16
    global _start
    _start:
        clear rax
        clear rbx
        clear rcx
        clear rdi
        mov rsi,rsp
        lea rdx,[rel flag]
        inc rdi
    _loop2:
        mov bl,cl
        inc bl
        xor bl,0xf0
        mov al,BYTE [rsi+rcx*1]
        xor al,bl
        cmp al,[rdx+rcx*1]
        jne _exit
        inc cl
        cmp cl,0x1e
        jl _loop2
        clear rdi

    _exit:
        clear rax
        mov al,0x3c
        syscall
        
    flag:
        db 0xb7, 0xbe, 0xb2, 0xb3, 0xd8, 0x92, 0xc6, 0x9c, 0xa6, 0x8f, 0xa4, 0x8c, 0xc9, 0xc9, 0x9c, 0x88, 0xbe, 0x96, 0x8b, 0xd7, 0xba, 0x84, 0xd6, 0x86, 0xdd, 0x98, 0x92, 0xd3, 0xd7, 0xc7