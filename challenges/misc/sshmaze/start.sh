#!/bin/bash

if [ -d "./home" ]; then
  echo "Please delete the home folder" 1>&2
  exit 1
fi

# NEED PYTHON 3.9 TO BE INSTALLED
python3 bakechall.py 10 10 0 0 3 2 1337 | tee maze.txt

# takes around 3-5 mins to start and stop
docker build -t sshmaze build 1>/dev/null
docker compose up --build -d
