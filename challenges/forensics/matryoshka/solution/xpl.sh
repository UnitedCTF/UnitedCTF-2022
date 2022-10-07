#!/bin/bash
set -e

ARCHIVE=matryoshka.zip
TMP=tmp.zip

while [ -e $ARCHIVE ]; do
    mv $ARCHIVE $TMP
    zip2john $TMP > hash.txt
    password=$(john hash.txt --mask="m4try0shk4#[A-Za-z][A-Za-z]?d?d?d?d" 2>/dev/null | tail -n1 | cut -d" " -f1)
    unzip -P "$password" $TMP
done