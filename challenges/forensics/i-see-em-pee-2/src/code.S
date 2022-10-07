.global _start
.text
    _start:
        mov $flag,%rsi
        xor %rcx,%rcx
    loop:
        mov (%rsi,%rcx,1),%al
        xor $42,%al
        mov %al,(%rsi,%rcx,1)
        inc %rcx
        cmp $flag_len,%rcx
        jle loop

        xor %rax,%rax
        inc %al
        mov %rax,%rdi
        mov $flag,%rsi
        mov $flag_len,%rdx
        syscall

        mov $0x3c,%al
        xor %rdi,%rdi
        syscall
.data
    flag: .byte 108, 102, 107, 109, 7, 94, 66, 27, 89, 117, 73, 26, 95, 70, 78, 13, 92, 25, 117, 72, 25, 25, 68, 117, 89, 26, 71, 25, 94, 66, 27, 68, 77, 117, 71, 30, 70, 27, 73, 67, 26, 95, 89
    .set flag_len, .-flag
