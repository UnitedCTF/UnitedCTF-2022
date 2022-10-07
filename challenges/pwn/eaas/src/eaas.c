#include <stdio.h>
#include <stdlib.h>
#include "shared.h"

#define BUFF_SIZE 128

void banner() {
    system("/bin/cat /challenge/banner.txt");
}

void main(int argc, char *argv[], char *envp[]) {
    char buff[BUFF_SIZE];

    init();
    banner();

    for (;;) {
        printf(fgets(buff, BUFF_SIZE, stdin));
    }
}