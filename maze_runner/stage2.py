"""
Labyrinth generation using Prim's algorithm from the video:
https://www.youtube.com/watch?v=cQVH4gcb3O4
"""

import random
from typing import NamedTuple
import time

# random.seed(37)  # always get the same maze


class Cell(NamedTuple):
    x: int
    y: int


class Maze:
    def __init__(self, height: int, width: int):
        # min_size = 4 x 4
        # print(f"Created maze: {height}x{width}")
        self.maze = [[1 for x in range(width)] for y in range(height)]
        self.height = height
        self.width = width
        self.maze_cells = set()
        self.frontier_cells = set()
        # self.print_maze()
        starting_point = self.generate_entrance(height)
        # self.maze_cells.append(starting_point)
        # self.print_maze()
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
        # print("----------")

    def generate_entrance(self, height):
        """
        Entrance X (column) always equals to 0, since it is the first column.
        And the Y (row) is randomly chosen.
        """
        entrance_y = random.choice([i for i in range(1, height - 1)])
        return Cell(0, entrance_y)

    def add_exit(self):
        """
        Entrance X (column) always equals to width - 1, since it is the last column.
        But it can happen, that the between exit and the maze there is wall, which
        also should be added.
        And the Y (row) is randomly chosen from the existing maze cells in the last column.
        """

        # search for the maze cells in the last column
        check_column = self.width - 2
        cell_candidates = []
        while len(cell_candidates) == 0:
            for cell in self.maze_cells:
                if cell.x == check_column:
                    cell_candidates.append(cell)
            check_column -= 1

        exit_cell = random.choice(cell_candidates)
        self.add_cell_to_maze(Cell(exit_cell.x + 1, exit_cell.y))
        if exit_cell.x + 1 < self.width - 1:
            self.add_cell_to_maze(Cell(exit_cell.x + 2, exit_cell.y))

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
                # print(f"Skipping the cell{cell_check}")
                continue
            # check that cell is not already in maze and not in frontier cells
            # print(
            #     f"Cell {cell_check} in {self.maze_cells} is {cell_check in self.maze_cells}"
            # )
            if cell_check in self.maze_cells or cell_check in self.frontier_cells:
                # print(f"Skipping the cell{cell_check}")
                continue
            else:
                # print(f"Added cell {cell_check}")
                result.add(cell_check)

        return result
        # while True:
        #     if
        # return frontier_cells

    def add_cell_to_maze(self, cell: Cell):
        """
        Adds cell to the maze and makes it pass.
        """
        self.maze[cell.y][cell.x] = 0
        self.maze_cells.add(cell)

        # self.print_maze() # UNCOMMENT HERE FOR NICE VISUALIZATION

    # def remove_frontier_cell(self, cell_to_remove):
    #     for cell in self.frontier_cells:
    #         if cell == cell_to_remove:

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

        self.add_exit()


if __name__ == "__main__":
    # maze = Maze(10, 10)

    maze_input = input("Please, enter the size of a maze\n")
    maze_input = maze_input.split(" ")
    Maze(int(maze_input[0]), int(maze_input[1]))
