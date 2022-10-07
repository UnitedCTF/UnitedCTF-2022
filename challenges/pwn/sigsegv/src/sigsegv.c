#include <sys/sendfile.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>
#include <stddef.h>
#include <stdio.h>
#include <fcntl.h>
#include "shared.h"

void sigsegv_handler();

int main() {
    char buff[32];

    init();

    signal(SIGSEGV, sigsegv_handler);

    puts("Welcome to BOF 101, this is an introduction to stack-based buffer overflows on x86-64.\n");
    puts("Objective 1: Cause a Segmentation Fault.");
    puts("Objective 2: Redirect the program's execution flow to the `win1` function.");
    puts("Objective 3: Redirect the program's execution flow to the `win2` function (be careful though, it expects 2 arguments).\n");
    puts("PIE is disabled, meaning the address of `win1` and `win2` will be predictable for you ahead of execution.\n");

    printf("Now, it's stack smashing time: ");
    gets(buff);
}

void sigsegv_handler() {
    int fd = open("/flag1", O_RDONLY);
    if (fd == -1) {
        perror("open");
        exit(EXIT_FAILURE);
    }
    sendfile(STDOUT_FILENO, fd, 0, FLAG_SIZE);
    close(fd);

    exit(EXIT_SUCCESS);
}

asm(".rept 213; nop; .endr");

void win1() {
    int fd = open("/flag2", O_RDONLY);
    if (fd == -1) {
        perror("open");
        exit(EXIT_FAILURE);
    }
    sendfile(STDOUT_FILENO, fd, 0, FLAG_SIZE);
    close(fd);

    exit(EXIT_SUCCESS);
}

void win2(unsigned long x, unsigned long y) {
    if ((x ^ y) != 0x1337133713371337) {
        exit(EXIT_FAILURE);
    }

    int fd = open("/flag3", O_RDONLY);
    if (fd == -1) {
        perror("open");
        exit(EXIT_FAILURE);
    }
    sendfile(STDOUT_FILENO, fd, 0, FLAG_SIZE);
    close(fd);

    exit(EXIT_SUCCESS);
}
