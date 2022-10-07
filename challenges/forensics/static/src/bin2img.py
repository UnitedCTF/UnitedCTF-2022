#!/usr/bin/env python3

import math
import os
import sys

from PIL import Image
import numpy as np

def bin2img(src, out):
  with open(src, "rb") as file:
    data = file.read()
  d = math.ceil(math.sqrt(len(data)/3))

  # pad our data so it first our np RGB array
  data += b"\x00" * ((d * d * 3) - len(data))

  # reshape the data into a np RGB array
  arr = np.frombuffer(data, dtype=np.uint8)
  arr = arr.reshape((d, d, 3))

  # rotate the arr (can't be too easy >:))
  arr = np.swapaxes(arr, 0, 1)

  # save the image
  im = Image.fromarray(np.uint8(arr))
  im.save(out)

def img2bin(src, out):
  im = Image.open(src)

  # convert the image to a np array
  arr = np.asarray(im)

  # rotate back the arr
  arr = np.swapaxes(arr, 0, 1)

  # flatten the RGB to bytes
  arr = arr.flatten()
  data = arr.tobytes()   

  # write the data to a file
  with open(out, "wb") as file:
    file.write(data)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Missing input argument")
    sys.exit(1)
  if not os.path.isfile(sys.argv[1]):
    print(f"File '{sys.argv[1]}' not found")
    sys.exit(1)

  if sys.argv[0].endswith("/bin2img.py"):
    bin2img(sys.argv[1], sys.argv[1]+".png")
  elif sys.argv[0].endswith("/img2bin.py"):
    img2bin(sys.argv[1], ".".join(sys.argv[1].split(".")[:1]))
  else:
    print("Unknown command")
    sys.exit(1)

