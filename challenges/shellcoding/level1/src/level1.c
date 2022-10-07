#include <sys/mman.h>
#include <seccomp.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>

#define MESSAGE "Welcome to Shellcoding Level 1!\n\n" \
                "I've banned all syscalls, except `open`, `read`, `write`, `close`, `exit` and `exit_group`.\n" \
                "Let me see your shellcode.\n" \
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

    scmp_filter_ctx ctx = seccomp_init(SCMP_ACT_KILL);

    void *shellcode = mmap(
        NULL, MEMSIZE, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0
    );
    read(STDIN_FILENO, shellcode, MEMSIZE);

    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, __NR_open, 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, __NR_read, 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, __NR_write, 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, __NR_close, 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, __NR_exit, 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, __NR_exit_group, 0);

    seccomp_load(ctx);
    seccomp_release(ctx);
  
    ((void (*)())shellcode)();

    return EXIT_SUCCESS;
}
