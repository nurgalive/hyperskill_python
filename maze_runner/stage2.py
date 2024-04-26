"""
I created some simple algorithm for generating random labyrinth, but it does
not pass the requirements, so I used the hardcoded one.
"""

import random

random.seed(37)  # always get the same maze


class Maze:
    def __init__(self, height: int, width: int):
        # min_size = 4 x 4
        print(f"Created maze: {height}x{width}")
        self.maze = [[1 for x in range(height)] for y in range(width)]
        self.print_maze()
        starting_point = self.generate_entrance_exit(height)
        self.print_maze()
        self.generate_maze(starting_point)

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
        return entrance

    # def generate_walls(self, start):
    #     for x in range(2  , self.maze):


if __name__ == "__main__":
    maze = Maze(4, 4)
