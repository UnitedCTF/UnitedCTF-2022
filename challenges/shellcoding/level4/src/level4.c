#include <sys/mman.h>
#include <seccomp.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>

#define MESSAGE "Welcome to Shellcoding Level 4!\n\n" \
                "Help me find the lost egg in memory.\n\n" \
                "> "
#define FLAG_FILE "/flag"
#define FLAG_SIZE 0x40
#define MEMSIZE 0x1000

void init() {
    char *flag = (char *)mmap(
        NULL, MEMSIZE, PROT_READ | PROT_WRITE, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0
    );
    int fd = open(FLAG_FILE, O_RDONLY);

    if (fd == -1) {
        perror("couldn't open flag file");
        exit(EXIT_FAILURE);
    }
    if (read(fd, flag, FLAG_SIZE) == -1) {
        perror("couldn't read flag content");
        close(fd);
        exit(EXIT_FAILURE);
    }
    flag = NULL;
    close(fd);

    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    printf(MESSAGE);
}

int main() {
    init();

    scmp_filter_ctx ctx = seccomp_init(SCMP_ACT_KILL);

    void *shellcode = mmap(
        (void *)0x31337000, MEMSIZE, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0
    );
    read(STDIN_FILENO, shellcode, MEMSIZE);

    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, __NR_write, 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, __NR_mmap, 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, __NR_exit, 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, __NR_exit_group, 0);

    seccomp_load(ctx);
    seccomp_release(ctx);
  
    ((void (*)())shellcode)();

    return EXIT_SUCCESS;
}   