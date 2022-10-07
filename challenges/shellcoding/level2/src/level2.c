#include <sys/mman.h>
#include <seccomp.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>

#define MESSAGE "Welcome to Shellcoding Level 2!\n\n" \
                "I made sure to only allow `close`, `stat`, `fstat`, `lstat`, `exit` and `exit_group` this time, " \
                "which shouldn't be useful for you to read the flag, right?\n\n" \
                "> "
#define MEMSIZE 0x1000

void init() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    printf(MESSAGE);
}

int main() {
    init();

    scmp_filter_ctx ctx = seccomp_init(SCMP_ACT_ALLOW);

    void *shellcode = mmap(
        (void *)0x31337000, MEMSIZE, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0
    );
    read(STDIN_FILENO, shellcode, MEMSIZE);

    for (int i = 0; i < 512; i++) {
        switch (i) {
            case __NR_close:
                continue;
            case __NR_stat:
                continue;
            case __NR_fstat:
                continue;
            case __NR_lstat:
                continue;
            case __NR_exit:
                continue;
            case __NR_exit_group:
                continue;
        }
        seccomp_rule_add(ctx, SCMP_ACT_KILL, i, 0);
    }

    seccomp_arch_add(ctx, SCMP_ARCH_X86);
    seccomp_load(ctx);
    seccomp_release(ctx);
  
    ((void (*)())shellcode)();

    return EXIT_SUCCESS;
}   
