#include <unistd.h>
#include <string.h>

int main() {
    const char *flag = "FLAG-str1ngsftw!";
    char input[32];

    write(STDOUT_FILENO, "~~ Flag checker v1.0 ~~\n", 24);
    write(STDOUT_FILENO, "Give me your input: ", 20);
    read(STDIN_FILENO, input, sizeof(input));
    input[strcspn(input, "\n")] = '\0';

    if (!strcmp(input, flag)) {
        write(STDOUT_FILENO, "Correct!", 8);
    } else {
        write(STDOUT_FILENO, "Wrong :(", 8);
    }

    return 0;
}