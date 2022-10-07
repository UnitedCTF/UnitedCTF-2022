.global _start
.intel_syntax noprefix

.text
    _start:
        lea rdi,[rip+0x53]
        xor rcx,rcx
    loop:
        mov al,[rdi+rcx]
        mov bl,cl
        inc bl
        xor al,bl
        mov [rdi+rcx],al
        inc cl
        cmp cl,25
        jle loop
        /* open("/dev/null", O_RDWR); */
        xor rax,rax
        mov al,2
        mov rsi,rax
        mov rdi,0x6c
        push rdi
        mov rdi,0x6c756e2f7665642f
        push rdi
        mov rdi,rsp
        syscall

        /* write(fd, flag, flag_length); */
        mov rdi,rax
        xor rax,rax
        inc al
        lea rsi,[rip+0xe]
        mov rdx,26
        syscall

        /* return to main */
        add rsp,0x10
        ret

    flag: .byte 71, 78, 66, 67, 40, 98, 54, 108, 122, 58, 102, 63, 98, 96, 60, 99, 37, 107, 99, 96, 103, 34, 116, 125, 38, 37, 0
