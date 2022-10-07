SHELL=/bin/bash

CC=gcc
CFLAGS=-Wl,-z,noseparate-code -no-pie
LDFLAGS=-lseccomp
LEVEL0=level0
LEVEL1=level1
LEVEL2=level2
LEVEL3=level3
LEVEL4=level4
CHALLENGES=$(LEVEL0) $(LEVEL1) $(LEVEL2) $(LEVEL3) $(LEVEL4)

.PHONY: $(CHALLENGES)

all: $(CHALLENGES)

$(LEVEL0): $(LEVEL0)/src/$(LEVEL0).c
	cd $(LEVEL0) && \
	mkdir -p challenge && \
	$(CC) src/$(LEVEL0).c $(CFLAGS) -o challenge/$(LEVEL0)

$(LEVEL1): $(LEVEL1)/src/$(LEVEL1).c
	cd $(LEVEL1) && \
	mkdir -p challenge && \
	$(CC) src/$(LEVEL1).c $(LDFLAGS) $(CFLAGS) -o challenge/$(LEVEL1)

$(LEVEL2): $(LEVEL2)/src/$(LEVEL2).c
	cd $(LEVEL2) && \
	mkdir -p challenge && \
	$(CC) src/$(LEVEL2).c $(LDFLAGS) $(CFLAGS) -o challenge/$(LEVEL2)

$(LEVEL3): $(LEVEL3)/src/$(LEVEL3).c
	cd $(LEVEL3) && \
	mkdir -p challenge && \
	$(CC) src/$(LEVEL3).c $(LDFLAGS) $(CFLAGS) -o challenge/$(LEVEL3)

$(LEVEL4): $(LEVEL4)/src/$(LEVEL4).c
	cd $(LEVEL4) && \
	mkdir -p challenge && \
	$(CC) src/$(LEVEL4).c $(LDFLAGS) $(CFLAGS) -o challenge/$(LEVEL4)
