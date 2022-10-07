#include <sys/mman.h>
#include <stdlib.h>
#include <unistd.h>
#include <stddef.h>
#include <stdio.h>

#define MESSAGE "Welcome to Shellcoding Level 0 - (In)Sanity check!\n\n" \
                "Just send me your shellcode and I'll happily execute it :)\n\n" \
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

    void *shellcode = mmap(
        NULL, MEMSIZE, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0
    );
    read(STDIN_FILENO, shellcode, MEMSIZE);
    ((void (*)())shellcode)();

    return EXIT_SUCCESS;
}
