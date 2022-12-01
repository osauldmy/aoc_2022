#!/bin/env python3
import pathlib


with open(pathlib.Path(__file__).parent / "day_01.input.txt") as f:
    data = f.read()

elves_carriages = tuple(
    map(lambda x: tuple(map(int, x.strip("\n").split("\n"))), data.split("\n\n"))
)

# First puzzle answer
print(sum(max(elves_carriages, key=sum)))

# Second puzzle answer
print(sum(map(sum, sorted(elves_carriages, key=sum, reverse=True)[:3])))
