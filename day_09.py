#!/bin/env python3
import operator
import pathlib


chebyshev = lambda x1, x2: max(map(abs, map(operator.sub, x1, x2)))

with open(pathlib.Path(__file__).parent / "day_09.input.txt") as f:
    data = f.read().strip("\n").split("\n")

moves = tuple(map(lambda x: (x.split(" ")[0], int(x.split(" ")[1])), data))

head, tail = [0, 0], (0, 0)
tail_visited = {tail}
for way, steps in moves:
    for _ in range(steps):
        old_head = tuple(head)
        head[way in ("U", "D")] += 1 if way in ("D", "R") else -1
        if chebyshev(head, tail) > 1:
            tail = old_head
            tail_visited.add(tail)

# First puzzle answer
print(len(tail_visited))

# Second puzzle answer
print("todo")
