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
        self.frontier_cells = set()
        self.print_maze()
        starting_point = self.generate_entrance_exit(height)
        # self.maze_cells.append(starting_point)
        self.print_maze()
        self.generate_maze(starting_point)

    def print_maze(self):
        """
        Converts array's zeros and ones into the visual
        representation and prints the maze.
        """
        for line in self.maze:
            for obj in line:
                if obj == 1:
                    print("██", sep="", end="")
                if obj == 0:
                    print("  ", sep="", end="")
            print("")
        print("----------")

    def generate_entrance_exit(self, height):
        """
        Entrance X (column) always equals to 0, since it is the first column.
        And the Y (row) is randomly chosen.
        """
        entrance_y = random.choice([i for i in range(1, height - 1)])
        self.maze[entrance_y][0] = 0
        return Cell(0, entrance_y)

    # frontier is
    # inside the grid
    # is not part of the maze

    def check_frontier(self, cell: Cell):
        pass

    def calculate_frontier(self, cell: Cell) -> set:
        return set()
        # while True:
        #     if
        # return frontier_cells

    def add_cell_to_maze(self, cell: Cell):
        """
        Adds cell to the maze and makes it pass.
        """
        self.maze[cell.x][cell.y] = 0
        self.maze_cells.append(cell)

    # def remove_frontier_cell(self, cell_to_remove):
    #     for cell in self.frontier_cells:
    #         if cell == cell_to_remove:

    def add_cell_closest_to_frontier(self, frontier_cell: Cell):
        """
        Check for the neighbour cells and merge the closes
        find the closest cell and merge with it
        """

        self.maze_cells

        # x                   # y
        frontier_cell[0] - 1, frontier_cell[1] - 1
        return []

    def generate_maze(self, starting_point):
        """
        1. Get the random (start) cell
        2. Calculate the frontier cells from the random (current) cell
        2.a. Add random cell to the maze and convert it to the pass
        3. Choose an arbitrary (произвольный) frontier cell from the frontier cells
        4. Draw the pass from the closest maze cell to the chosen random frontier
        4.a. How to find the closes cell?
        5. Remove this frontier from the frontier list
        6. Repeat 2 - 5
        """

        # # initializing the algorithm with the entrance (starting point)
        # # adding frontier cells
        # self.frontier_cells.update(self.calculate_frontier(starting_point))
        # # adding the starting point to the maze and making it as a passage
        # self.add_cell_to_maze(starting_point)
        # # choosing an arbitrary frontier, which is for the starting point only one
        # arbitrary_frontier = random.choice(tuple(self.frontier_cells))
        # # adding a passage between frontier and a closest maze cell
        # self.add_cell_closest_to_frontier(arbitrary_frontier)
        # # remove the frontier cell from the frontier cells
        # self.frontier_cells.remove(arbitrary_frontier)

        arbitrary_frontier = starting_point
        self.add_cell_to_maze(arbitrary_frontier)
        self.frontier_cells.update(self.calculate_frontier(arbitrary_frontier))
        while self.frontier_cells:
            arbitrary_frontier = random.choice(tuple(self.frontier_cells))
            self.add_cell_to_maze(arbitrary_frontier)
            self.add_cell_closest_to_frontier(arbitrary_frontier)

            self.frontier_cells.update(
                self.calculate_frontier(arbitrary_frontier)
            )  # calculate frontier from the start
            self.frontier_cells.remove(arbitrary_frontier)

            # choose arbitrary frontier

        # rewrite the code using recursion
        # def front(self, ):
        #     if self.frontier_cells:
        #         return
        #     else

        #### backup
        # current_cell = starting_point
        # self.frontier_cells.update(self.calculate_frontier(current_cell))
        # while self.frontier_cells:
        #     self.frontier_cells.update(
        #         self.calculate_frontier(current_cell)
        #     )  # calculate frontier from the start

        #     self.add_cell_to_maze(current_cell)
        #     # choose arbitrary frontier
        #     current_cell = random.choice(tuple(self.frontier_cells))
        #     self.add_cell_closest_to_frontier(current_cell)
        #     self.frontier_cells.remove(current_cell)

        # self.maze_cells.append(
        #     self.add_cells_to_maze(self.maze_cells[0])
        # )  # add current frontier and cell in between to the maze
        # self.maze_cells.remove()


if __name__ == "__main__":
    maze = Maze(4, 4)
