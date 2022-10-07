#!/bin/bash
set -e

OUTDIR=dist
TMP=tmp.zip
LAST=flag.txt
ITERATIONS=256
ARCHIVE=matryoshka.zip

for i in $(seq 1 $ITERATIONS); do
    a=$(cat /dev/urandom | tr -dc A-Za-z | fold -w2 | head -n1)
    b=$(cat /dev/urandom | tr -dc 0-9 | fold -w4 | head -n1)
    password="m4try0shk4#${a}${b}"
    zip -P "$password" $TMP $LAST
    mv $TMP $ARCHIVE
    LAST=$ARCHIVE
done

mv $ARCHIVE $OUTDIR/$ARCHIVE