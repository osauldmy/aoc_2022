#!/bin/env python3
import itertools
import pathlib


with open(pathlib.Path(__file__).parent / "day_10.input.txt") as f:
    data = f.read().strip("\n").split("\n")


X, log = 1, []
for instruction in data:
    match instruction.split(" "):
        case "noop",:
            log.append(X)
        case "addx", value:
            log.extend((X, X))
            X += int(value)

# First puzzle answer
print(sum(map(lambda cycle: cycle * log[cycle - 1], range(20, 221, 40))))

# Second puzzle answer
line = ["."] * 40
for index, x in zip(itertools.cycle(range(0, 40)), log):
    line[index] = "#" if index in (x - 1, x, x + 1) else "."
    if index == 39:
        print(" ".join(line))
        line = ["."] * 40
