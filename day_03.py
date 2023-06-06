#!/usr/bin/env python3
import functools
import pathlib
import string

import more_itertools


with open(pathlib.Path(__file__).parent / "input" / "day_03.txt") as f:
    rucksacks = f.read().strip("\n").split("\n")

priorities = dict(zip(string.ascii_letters, range(1, len(string.ascii_letters) + 1)))

halfstrings_intersects = map(
    lambda s: (set(s[len(s) // 2 :]) & set(s[: len(s) // 2])).pop(), rucksacks
)

# First puzzle answer
print(sum(map(priorities.get, halfstrings_intersects)))

triplewise_intersects = map(
    lambda x: functools.reduce(set.intersection, x).pop(),
    more_itertools.chunked(map(set, rucksacks), 3),
)

# Second puzzle answer
print(sum(map(priorities.get, triplewise_intersects)))
