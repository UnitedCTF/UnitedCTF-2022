#!/usr/bin/python3
from mazelib.solve.ShortestPath import ShortestPath
from mazelib.generate.Prims import Prims
from mazelib import Maze
from pwn import *
import numpy as np

RHOST, RPORT = "nc.ctf.unitedctf.ca", 5001

r = remote(RHOST, RPORT)

txt = [r.recvline().decode().strip() for _ in range(21)]
grid = np.array(
    [[1 if cell == "#" else 0 for cell in row] for row in txt], dtype="int8"
)

m = Maze()
m.generator = Prims(10, 10)
m.solver = ShortestPath()
m.grid = grid

for c, row in enumerate(txt):
    if "S" in row:
        m.start = (c, row.index("S"))
    elif "E" in row:
        m.end = (c, row.index("E"))

m.solve()

for xy in m.solutions[0]:
    r.sendline(f"{xy[0]} {xy[1]}".encode())

r.sendline(b".")

flag = r.recvline().decode()
r.success(flag)
