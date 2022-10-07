#!/bin/bash
set -e

# Make our flag dynamic
export BASE64_FLAG=`cat flag.txt | base64`
envsubst < ./src/flag.go > "flag.go"
go build flag.go
rm flag.go

# Generate the flag image from the binary
./src/bin2img.py flag
rm flag

echo "Generated the challenge in 'flag.png'"
