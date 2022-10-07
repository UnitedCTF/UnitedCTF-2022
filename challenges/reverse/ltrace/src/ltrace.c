#define _GNU_SOURCE
#include <unistd.h>
#include <string.h>

int main() {
    char flag[] = { 108, 102, 107, 109, 7, 70, 27, 72, 88, 30, 88, 83, 73, 30, 70, 70, 94, 88, 30, 73, 27, 68, 77, 76, 94, 93, 11, 0 };
    char input[32];

    write(STDOUT_FILENO, "~~ Flag checker v1.1 ~~\n", 24);
    write(STDOUT_FILENO, "Give me your input: ", 20);
    read(STDIN_FILENO, input, sizeof(input));
    input[strcspn(input, "\n")] = '\0';

    memfrob(flag, 27);

    if (!strcmp(input, flag)) {
        write(STDOUT_FILENO, "Correct!", 8);
    } else {
        write(STDOUT_FILENO, "Wrong :(", 8);
    }

    return 0;
}