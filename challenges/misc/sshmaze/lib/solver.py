from queue import PriorityQueue
import sys

from lib.maze import Maze


class Solver:
  def __init__(self, maze: "Maze") -> None:
    self.maze = maze

  def aStar(self):
    maze = self.maze

    start = (maze.sx, maze.sy)
    g_score = { (x, y): float("inf") for x in range(maze.nx) for y in range(maze.ny) }
    g_score[start] = 0
    f_score = { (x, y): float("inf") for x in range(maze.nx) for y in range(maze.ny) }

    def h(cell1, cell2):
      x1, y1 = cell1
      x2, y2 = cell2

      return abs(x1 - x2) + abs(y1 - y2)

    f_score[start] = h(start, (1, 1))

    open = PriorityQueue()
    open.put((h(start, (1, 1)), h(start, (1, 1)), start))
    aPath = {}

    while not open.empty():
      currCell = open.get()[2]
      if currCell == (maze.ex, maze.ey):
        break
      for d in "ESNW":
        if not self.maze.cell_at(currCell[0], currCell[1]).walls[d]:
          if d == "E":
            childCell = (((currCell[0]+1 + maze.nx) % maze.nx), currCell[1])
          if d == "W":
            childCell = (((currCell[0]-1 + maze.nx) % maze.nx), currCell[1])
          if d == "N":
            childCell = (currCell[0], ((currCell[1]-1 + maze.ny) % maze.ny))
          if d == "S":
            childCell = (currCell[0], ((currCell[1]+1 + maze.ny) % maze.ny))

          temp_g_score = g_score[currCell] + 1
          temp_f_score = temp_g_score + h(childCell, (1, 1))

          if temp_f_score < f_score[childCell]:
            g_score[childCell] = temp_g_score
            f_score[childCell] = temp_f_score
            open.put((temp_f_score, h(childCell, (1, 1)), childCell))
            aPath[childCell] = currCell
    
    fPath = []
    cell = (maze.ex, maze.ey)
    while True:
      cell = aPath[cell]
      if cell == start:
        break
      fPath += (cell,)
    return fPath[::-1]
