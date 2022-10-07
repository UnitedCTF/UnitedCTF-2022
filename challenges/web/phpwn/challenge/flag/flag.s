.global _start
.text
    _start:
        /* write(STDOUT_FILENO, flag, flag_len); */
        xor %rax,%rax
        inc %al
        mov %rax,%rdi
        mov $flag,%rsi
        mov $flag_len,%rdx
        syscall

        /* exit(0); */
        mov $0x3c,%al
        xor %rdi,%rdi
        syscall

    flag: .ascii "FLAG-798fc96f7f917fb6f398214bf5d59552b6823c16f6b89675\n"
    .set flag_len, .-flag
