import random

# print('\u2588\u2588', end = '')  # wall
# print("  ")  # pass

# generate array 10 x 10 using random with values 1 and 0
# convert 1 and 0 to space and block ██

# 10 x 10
# maze_init = [[random.randint(0, 1) for j in range(10)] for i in range(10)]
random.seed(3)
entrance = random.choice([i for i in range(1, 9)])
exit = random.choice([i for i in range(1, 9)])
print("entrance:", entrance, "exit:", exit)
maze_init = []
for i in range(10):
    maze_init.append([])
    for j in range(10):
        if i == 0 or i == 9:  # first and last line have to be solid
            maze_init[i].append(1)
        else:
            if i == entrance and j == 0:
                maze_init[i].append(0)  # append 0, if line equals entrance
            elif j == 0:
                maze_init[i].append(1)  # first column should have only one entrance
            elif i == exit and j == 9:  # TODO: hardcoded
                maze_init[i].append(0)  # append 0, if line equals exit
            elif j == 9:
                maze_init[i].append(1)  # last column should have only one exit
            maze_init[i].append(random.randint(0, 1))  # generate pass (0) or wall (1)

print(maze_init)

for line in maze_init:
    for obj in line:
        if obj == 1:
            print("██", sep="", end="")
        if obj == 0:
            print("  ", sep="", end="")
    print("")

# class Maze:
#     def __init__(x: int, y: int):
#         maze_init = [[random.randint(0, 1) for j in range(10)] for i in range(10)]
#         maze = []

print(
    """
████████████████████
    ██  ██  ██    ██
██  ██      ██  ████
██      ██████
██  ██          ████
██  ██  ██████  ████
██  ██  ██      ████
██  ██  ██████  ████
██  ██      ██    ██
████████████████████
"""
)
