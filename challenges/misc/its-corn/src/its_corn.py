from mazelib import Maze
from mazelib.generate.Prims import Prims
from mazelib.solve.ShortestPath import ShortestPath
import signal
import os

TIMEOUT = 3
MAZE_HEIGHT = int(os.getenv("MAZE_HEIGHT") or 10)
MAZE_WIDTH = int(os.getenv("MAZE_WIDTH") or 10)
FLAG = os.getenv("FLAG") or "FLAG-testflag"


def generate_maze():
    err_msg = "Oops. Try again."

    m = Maze()
    m.generator = Prims(MAZE_HEIGHT, MAZE_WIDTH)
    m.generate()
    m.generate_entrances(True, True)
    print(m.tostring(True, False))
    m.solver = ShortestPath()
    m.solve()
    s = "\n".join(map(str, m.solutions[0]))
    s = s.replace("(", "").replace(")", "").replace(",", "").split("\n")

    i = 0
    while True:
        coord = input().strip()
        if coord == "." and i == len(s):
            print(FLAG)
            break
        else:
            try:
                if s[i] != coord:
                    print(err_msg)
                    break
                i += 1
            except Exception as e:
                print(err_msg)
                break


def alarm_handler(signum, frame):
    print("Too slow!")
    exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(TIMEOUT)
    generate_maze()
