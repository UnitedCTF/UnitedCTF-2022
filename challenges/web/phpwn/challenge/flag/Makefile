CC=gcc
CFLAGS=-static -nostdlib
SOURCE=flag.s
OUTFILE=flag

all: $(SOURCE)
	$(CC) $(SOURCE) $(CFLAGS) -o $(OUTFILE)
	strip $(OUTFILE)
clean: $(OUTFILE)
	rm -f $(OUTFILE)
