"""
I created some simple algorithm for generating random labyrinth, but it does
not pass the requirements, so I used the hardcoded one.
"""

import random
from typing import NamedTuple

random.seed(37)  # always get the same maze


class Cell(NamedTuple):
    x: int
    y: int


class Maze:
    def __init__(self, height: int, width: int):
        # min_size = 4 x 4
        print(f"Created maze: {height}x{width}")
        self.maze = [[1 for x in range(height)] for y in range(width)]
        self.height = height
        self.width = width
        self.maze_cells = []
        self.frontier_cells = []
        self.print_maze()
        starting_point = self.generate_entrance_exit(height)
        self.maze_cells.append(starting_point)
        self.print_maze()
        self.generate_maze()

    def print_maze(self):
        for line in self.maze:
            for obj in line:
                if obj == 1:
                    print("██", sep="", end="")
                if obj == 0:
                    print("  ", sep="", end="")
            print("")
        print("----------")

    def generate_entrance_exit(self, height):
        entrance = random.choice([i for i in range(1, height - 1)])
        self.maze[entrance][0] = 0
        return entrance, 0

    # frontier is
    # inside the grid
    # is not part of the maze

    def check_frontier(self, x, y):
        pass

    def calculate_frontier(self, x: int, y: int):
        pass
        # while True:
        #     if
        # return frontier_cells

    def add_cells_to_maze(self, frontier_cell):
        # check for the neighbour cells and merge the closes
        # find the closest cell and merge with it
        self.maze_cells

        # x                   # y
        frontier_cell[0] - 1, frontier_cell[1] - 1
        return []

    def generate_maze(self):
        self.frontier_cells.append(
            self.maze_cells[0]
        )  # calculate frontier from the start
        self.maze_cells.append(
            self.add_cells_to_maze(self.maze_cells[0])
        )  # add current frontier and cell in between to the maze
        # self.maze_cells.remove()
        while self.frontier_cells:
            pass


if __name__ == "__main__":
    maze = Maze(4, 4)
