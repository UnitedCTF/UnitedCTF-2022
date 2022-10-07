#include <sys/sendfile.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>

#define FLAG_SIZE 54

typedef unsigned int uint;

typedef struct Item {
    char name[8];
    void (*pull_out)();
}Item;

typedef struct Pocket {
    struct Item *item;
}Pocket;

void pull_out_pen() {
    puts(
        "Oh hey, what did you expect? That's the pen I've been carrying with me before "
        "you were even born, nice try Jimmy, but I'm the BEST lawyer and I'll take you "
        "down SO YOU WON'T BE A LAWYER ANYMORE!!!"
    );
}

void chicanery() {
    puts("It's a battery...");
    sleep(2);
    puts("No... It's a trick. Must be...");
    sleep(2);
    puts("I am not crazy! I am not crazy.");
    sleep(1.5);
    puts(
        "I know he swapped those numbers! I knew it was 1216. One after Magna Carta! "
        "As if I would make such a mistake. Never. Never! I just, just couldn't prove "
        "it. He made sure of that! He covered his tracks, got that idiot at the copy "
        "shop to lie for him\n"
    );
    sleep(4);
    puts(
        "You think this is bad, this, this chicanery? He's done worse! That billboard! "
        "You're telling me a man just happens to fall like that? No -- he orchestrated "
        "that! Jimmy!\n"
    );
    sleep(4);
    puts(
        "He defecated through a sun roof! I saved him, but I shouldn't have. Took him "
        "into my own firm! What was I thinking!?\n"
    );
    sleep(3);
    puts(
        "He'll never change. Since he was nine, always the same! Couldn't keep his "
        "hands out of the cash drawer. But no, not Jimmy! It couldn't be precious "
        "Jimmy! Stealing them blind! And he gets to be a lawyer? What a sick joke!\n"
    );
    sleep(3);
    puts(
        "I should have stopped him when I had a chance. You, you have to stop him! "
        "You have to --!!\n"
    );
    sleep(4);
    int fd = open("/flag", O_RDONLY);
    if (fd == -1) {
        perror("open");
        exit(EXIT_FAILURE);
    }
    sendfile(STDOUT_FILENO, fd, 0, FLAG_SIZE);
    close(fd);
    exit(EXIT_SUCCESS);
}

uint read_int() {
	char tmp[16];
	fgets(tmp, sizeof(tmp), stdin);
	return (uint)atoi(tmp);
}

void init() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    puts(
        "As Jimmy's date with the state bar committee arrives, he and Kim set in "
        "motion a series of surprises for Chuck, and you, Mr. Babineaux, are here to help.\n"
        "Jimmy has one simple task for you: bump into his brother and sneak a fully "
        "charged battery on his breast pocket."
    );
}

void main() {
    init();

    Item *battery = NULL;

    Pocket *pocket = (Pocket *)malloc(sizeof(Pocket));
    pocket->item = (Item *)malloc(sizeof(Item));

    pocket->item->pull_out = pull_out_pen;
    strcpy(pocket->item->name, "pen");

    for (;;) {
        printf(
            "[1] (as Jimmy) Tell Chuck to land you his pen\n"
            "[2] (as Huell) Bump into Chuck and place a fully charged battery on his left breast pocket\n"
            "> "
        );

        switch (read_int()) {
            case 1:
                if (!strcmp(pocket->item->name, "pen")) {
                    pocket->item->pull_out();
                    free(pocket->item);
                }
                else
                    puts("I think I lost my pen, Jimmy, did you STEAL IT?!");
                break;

            case 2:
                if (battery == NULL)
                    battery = (Item *)malloc(sizeof(Item));

                printf("Psst, carefully forge the battery!\n> ");
                read(STDIN_FILENO, battery, sizeof(Item));
                break;

            default:
                puts("No such action");
                break;
        }
    }
}