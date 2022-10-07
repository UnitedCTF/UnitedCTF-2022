SHELL=/bin/bash

CC=gcc
CFLAGS=-Wl,-z,noseparate-code -Wno-implicit-function-declaration -I..
CFLAGS_x86=-m32
CFLAGS_NOASLR=-DNOASLR
CFLAGS_NOPIE=-no-pie -DNOPIE
CFLAGS_NODEP=-z execstack -DNODEP
CFLAGS_SSP=-fstack-protector -DSSP
CHALL1=sigsegv
CHALL2=ret2shellcode
CHALL4=ret2libc
CHALL7=chicanery
CHALL8=eaas

CHALLENGES=$(CHALL1) $(CHALL2) $(CHALL4) $(CHALL7) $(CHALL8)

.PHONY: $(CHALLENGES)

all: $(CHALLENGES)

$(CHALL1): $(CHALL1)/src/$(CHALL1).c shared.h
	cd $(CHALL1) && \
	mkdir -p challenge && \
	$(CC) src/$(CHALL1).c $(CFLAGS) $(CFLAGS_NOPIE) -o challenge/$(CHALL1)

$(CHALL2): $(CHALL2)/src/$(CHALL2).c shared.h
	cd $(CHALL2) && \
	mkdir -p challenge && \
	$(CC) src/$(CHALL2).c $(CFLAGS) $(CFLAGS_NOPIE) $(CFLAGS_NODEP) $(CFLAGS_x86) -o challenge/$(CHALL2)

$(CHALL4): $(CHALL4)/src/$(CHALL4).c shared.h
	cd $(CHALL4) && \
	mkdir -p challenge && \
	$(CC) src/$(CHALL4).c $(CFLAGS) $(CFLAGS_NOPIE) -o challenge/$(CHALL4)

$(CHALL7): $(CHALL7)/src/$(CHALL7).c
	cd $(CHALL7) && \
	mkdir -p challenge && \
	$(CC) src/$(CHALL7).c $(CFLAGS) $(CFLAGS_NOPIE) -o challenge/$(CHALL7)

$(CHALL8): $(CHALL8)/src/$(CHALL8).c
	cd $(CHALL8) && \
	mkdir -p challenge && \
	$(CC) src/$(CHALL8).c $(CFLAGS) $(CFLAGS_NOPIE) -o challenge/$(CHALL8)
