#include <stdio.h>
#include "shared.h"

void vuln() {
    char buff[128];
    
    printf("Here is your gift, you only have to smash me: %p\n> ", buff);
    gets(buff);
}

int main() {
    init();
    vuln();
}
