"""
Maze generation using Prim's algorithm from the video:
https://www.youtube.com/watch?v=cQVH4gcb3O4
"""

import random
from typing import NamedTuple
import time
import pickle

# random.seed(37)  # always get the same maze


class Cell(NamedTuple):
    """
    Class for storing the Cell object.
    """

    x: int  # height
    y: int  # width


class Maze:
    """
    Class which creates and stores the maze in form of square.
       __y: width___
    x:|
     h|
     e|
     i|
     g|
     h|
     t|______________
    """

    def __init__(self, size: int):
        # print(f"Created maze: {height}x{width}")
        self.maze = [[1 for x in range(size)] for y in range(size)]
        self.height = size
        self.width = size
        self.maze_cells = set()
        self.frontier_cells = set()
        starting_point = self.generate_entrance(size)
        self.generate_maze(starting_point)
        self.print_maze()

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
        time.sleep(0.01)
        print("----------")  # UNCOMMENT HERE FOR NICE VISUALIZATION

    def generate_entrance(self, height):
        """
        Entrance Y (column) always equals to 0, since it is the first column.
        And the X (row) is randomly chosen.
        """
        entrance_x = random.choice([i for i in range(1, height - 1)])
        return Cell(entrance_x, 0)

    def add_exit(self):
        """
        Entrance Y (column) always equals to width - 1, since it is the last column.
        But it can happen, that the between exit and the maze there is wall, which
        also should be added.
        And the X (row) is randomly chosen from the existing maze cells in the last column.
        """

        # search for the maze cells in the last column
        check_column = self.width - 2
        cell_candidates = []
        while len(cell_candidates) == 0:
            for cell in self.maze_cells:
                if cell.y == check_column:
                    cell_candidates.append(cell)
            check_column -= 1

        exit_cell = random.choice(cell_candidates)
        self.add_cell_to_maze(Cell(exit_cell.x, exit_cell.y + 1))
        if exit_cell.y + 1 < self.width - 1:
            self.add_cell_to_maze(Cell(exit_cell.x, exit_cell.y + 2))

    def calculate_frontier(self, cell: Cell) -> set:
        """
        Frontier cell, is a cell the inside grid in distance 2 from the
        start cell, not in the maze and not a frontier cell already.
        """
        result = set()
        cell_1 = Cell(cell.x + 2, cell.y)
        cell_2 = Cell(cell.x - 2, cell.y)
        cell_3 = Cell(cell.x, cell.y - 2)
        cell_4 = Cell(cell.x, cell.y + 2)
        cells_to_check = set([cell_1, cell_2, cell_3, cell_4])
        # add check, that it is inside the grid
        for cell_check in cells_to_check:
            # check that the cell is not goes outside the grid
            # height - 1 > x > 1 and width - 1 > y > 1
            if (
                cell_check.x > self.height - 2
                or cell_check.x < 1
                or cell_check.y > self.width - 2
                or cell_check.y < 1
            ):
                continue
            # checks that the potential frontier cell is not in the maze already
            if cell_check in self.maze_cells or cell_check in self.frontier_cells:
                continue
            else:
                result.add(cell_check)

        return result

    def add_cell_to_maze(self, cell: Cell):
        """
        Adds cell to the maze and makes it pass.
        """
        self.maze[cell.x][cell.y] = 0
        self.maze_cells.add(cell)

        self.print_maze()  # UNCOMMENT HERE FOR NICE VISUALIZATION

    def add_cell_closest_to_frontier(self, frontier_cell: Cell):
        """
        Check for the neighbors cells and merge the closes
        find the closest cell and merge with it.
        # 1. Check for the maze cells in four directions

        """
        cells_to_check = set(
            [
                Cell(frontier_cell.x + 2, frontier_cell.y),
                Cell(frontier_cell.x - 2, frontier_cell.y),
                Cell(frontier_cell.x, frontier_cell.y + 2),
                Cell(frontier_cell.x, frontier_cell.y - 2),
            ]
        )
        cells_to_choose = set()
        for cell in cells_to_check:
            if cell in self.maze_cells:
                cells_to_choose.add(cell)

        cell_to_connect = random.choice(list(cells_to_choose))

        cell_to_add = self.get_middle_cell(frontier_cell, cell_to_connect)
        self.add_cell_to_maze(cell_to_add)

    def get_middle_cell(self, cell_1: Cell, cell_2: Cell):
        """
        Calculate the middle cell between two cells.
        """
        middle_x = (cell_1.x + cell_2.x) // 2
        middle_y = (cell_1.y + cell_2.y) // 2
        return Cell(x=middle_x, y=middle_y)

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

        self.add_exit()


class MazeMenu:
    def __init__(self):
        self.head = ["=== Menu ===", "1. Generate a new maze", "2. Load a maze"]
        self.body = []
        self.add_exit()
        self.maze = None
        self.start()

    def add_exit(self):
        self.body.append("0. Exit")

    def start(self):
        while True:
            user_input = input("\n".join(line for line in self.head + self.body) + "\n")
            if user_input == "0":  # exit
                break
            if user_input == "1":  # generate a new maze
                pass
            if user_input == "2":  # load a maze
                pass
            else:
                print("Incorrect option. Please try again")
        # 3 - save the maze
        # 4 - display the maze

    def load_maze(self, path):
        pass


if __name__ == "__main__":
    # === Menu ===
    # 1. Generate a new maze
    # 2. Load a maze
    # 0. Exit

    # === Menu ===
    # 1. Generate a new maze
    # 2. Load a maze
    # 3. Save the maze
    # 4. Display the maze
    # 0. Exit

    # maze_input = input("Please, enter the size of a maze\n")
    # maze_input = maze_input.split(" ")
    # Maze(int(maze_input[0]))
    MazeMenu()
