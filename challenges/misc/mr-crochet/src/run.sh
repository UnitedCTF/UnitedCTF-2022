#!/bin/sh

git config --global user.name "Mr. Crochet"
git config --global user.email "mrcrochet@unitedctf.ca"
git config --global --add safe.directory /tmp

while :; do
    socat -dd -T60 tcp-l:1337,reuseaddr,fork,keepalive exec:"/challenge.sh",stderr
done
