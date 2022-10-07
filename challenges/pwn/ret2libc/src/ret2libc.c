#include <stdio.h>
#include <unistd.h>
#include "shared.h"

#define BUFF_SIZE 32

int main() {
    char buff[BUFF_SIZE];

    init();

    printf("> ");
    gets(buff);
}
