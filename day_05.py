#!/bin/env python3
import collections
import copy
import operator
import pathlib
import re

with open(pathlib.Path(__file__).parent / "input" / "day_05.txt") as f:
    text_stacks, text_moves = f.read().strip("\n").split("\n\n")

stacks_n = 9
stack_col_index = lambda i: 1 + 4 * (i - 1)
col = lambda i: tuple(row[i] for row in text_stacks.split("\n"))

stacks = tuple(
    map(
        lambda i: collections.deque(filter(str.isalpha, col(i))),
        map(stack_col_index, range(1, stacks_n + 1)),
    )
)

pattern = r"move (\d+) from (\d+) to (\d+)"
moves = tuple(map(lambda x: tuple(map(int, x)), re.findall(pattern, text_moves)))

backup = copy.deepcopy(stacks)
for (count, src, dest) in moves:
    stacks[dest - 1].extendleft(stacks[src - 1].popleft() for _ in range(count))

# First puzzle answer
print("".join(map(operator.itemgetter(0), stacks)))

stacks = backup
for (count, src, dest) in moves:
    stacks[dest - 1].extendleft(
        reversed(tuple(stacks[src - 1].popleft() for _ in range(count)))
    )

# Second puzzle answer
print("".join(map(operator.itemgetter(0), stacks)))
