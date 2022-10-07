import sys
import random
from time import time_ns


# Create a maze using the depth-first algorithm described at
# https://scipython.com/blog/making-a-maze/
# Christian Hill, April 2017.

class Cell:
  """A cell in the maze.

  A maze "Cell" is a point in the grid which may be surrounded by walls to
  the north, east, south or west.

  """

  # A wall separates a pair of cells in the N-S or W-E directions.
  wall_pairs = {"N": "S", "S": "N", "E": "W", "W": "E"}

  def __init__(self, x, y):
    """Initialize the cell at (x,y). At first it is surrounded by walls."""

    self.marker = " "
    self.x, self.y = x, y
    self.walls = {"N": True, "S": True, "E": True, "W": True}

  def has_all_walls(self):
    """Does this cell still have all its walls?"""

    return all(self.walls.values())

  def knock_down_wall(self, other, wall):
    """Knock down the wall between cells self and other."""

    self.walls[wall] = False
    other.walls[Cell.wall_pairs[wall]] = False

  def coords(self):
    return (self.x, self.y)


class Maze:
  """A Maze, represented as a grid of cells."""

  def __init__(self, nx, ny, sx, sy, ex, ey, seed=time_ns()):
    """Initialize the maze grid.
    The maze consists of nx x ny cells and will be constructed starting
    at the cell indexed at (ix, iy).

    """
    self.seed = seed
    random.seed(seed)

    self.nx, self.ny = nx, ny
    self.sx, self.sy = sx, sy
    self.ex, self.ey = ex, ey 

    self.maze_map = [[Cell(x, y) for y in range(self.ny)]
                     for x in range(self.nx)]
    self.cell_at(sx, sy).marker = "S"
    self.cell_at(ex, ey).marker = "E"

    self.__make_maze()

  def cell_at(self, x, y):
    return self.maze_map[(x + self.nx) % self.nx][(y + self.ny) % self.ny]

  def cell_neighbors(self, x, y):
    return [(direction, self.cell_at(x + dx, y + dy)) for direction, (dx, dy) in
            [("W", (-1, 0)),
             ("E", (1, 0)),
             ("S", (0, 1)),
             ("N", (0, -1))]]

  def cell_open_neighbors(self, x, y):
    return [(direction, neigh) for direction, neigh in self.cell_neighbors(x, y) if not self.cell_at(x, y).walls[direction]]

  def cell_closed_neighbors(self, x, y):
    return [(direction, neigh) for direction, neigh in self.cell_neighbors(x, y) if self.cell_at(x, y).walls[direction]]

  def __str__(self):
    maze_rows = [[]]
    for x in range(self.nx):
      maze_rows[0].append("+-" if self.cell_at(x, 0).walls["N"] else "+ ")
    maze_rows[0].append("+")

    for y in range(self.ny):
      maze_row = ["|" if self.cell_at(0, y).walls["W"] else " "]
      for x in range(self.nx):
        cell = self.cell_at(x, y)
        if cell.walls["E"]:
          maze_row += cell.marker + "|"
        else:
          maze_row += cell.marker + " "
      maze_rows.append(maze_row)

      if y + 1 >= self.ny:
        continue
      maze_row = ["+"]
      for x in range(self.nx):
        cell = self.cell_at(x, y)
        if cell.walls["S"]:
          maze_row += "-+"
        else:
          maze_row += " +"
      maze_rows.append(maze_row)

    maze_rows.append([])
    for x in range(self.nx):
      maze_rows[len(maze_rows)-1].append("+-" if self.cell_at(x,
                                                              self.ny - 1).walls["S"] else "+ ")
    maze_rows[len(maze_rows)-1].append("+")

    return "\n".join(["".join(row) for row in maze_rows])

  def __find_valid_neighbours(self, cell):
    delta = [("W", (-1, 0)),
             ("E", (1, 0)),
             ("S", (0, 1)),
             ("N", (0, -1))]

    neighbours = []
    for direction, (dx, dy) in delta:
      x2, y2 = cell.x + dx, cell.y + dy
      if (0 <= x2 < self.nx) and (0 <= y2 < self.ny):
        neighbour = self.cell_at(x2, y2)
        if neighbour.has_all_walls():
          neighbours.append((direction, neighbour))
    return neighbours

  def __make_maze(self):
    # Total number of cells.
    n = self.nx * self.ny
    cell_stack = []
    current_cell = self.cell_at(self.sx, self.sy)
    # Total number of visited cells during maze construction.
    nv = 1

    while nv < n:
      neighbours = self.__find_valid_neighbours(current_cell)

      if not neighbours:
        # We"ve reached a dead end: backtrack.
        current_cell = cell_stack.pop()
        continue

      # Choose a random neighbouring cell and move to it.
      direction, next_cell = random.choice(neighbours)
      current_cell.knock_down_wall(next_cell, direction)
      cell_stack.append(current_cell)
      current_cell = next_cell
      nv += 1

    # Go through all nodes an knock down some walls
    for x in range(self.nx):
      for y in range(self.ny):
        cell = self.cell_at(x, y)
        closed_neighs = self.cell_closed_neighbors(x, y)

        for direction, neigh in closed_neighs:
          if random.random() > 0.95:
            cell.knock_down_wall(neigh, direction)


if __name__ == "__main__":
  maze = Maze(*[int(arg) for arg in sys.argv[1:]])
  print(maze)
