#!/bin/env python3
import itertools
import operator
import pathlib

# Instead of dealing with splitting by 2 delimiters, change comma to dash
# and then split and map to int 4 integers which will represent start and end of
# each interval, then it's enough to look at them as (non-)sorted sequences.
with open(pathlib.Path(__file__).parent / "input" / "day_04.txt") as f:
    data = f.read().strip("\n").replace(",", "-").split("\n")

is_sorted = lambda x: all(itertools.starmap(operator.le, itertools.pairwise(x)))

intervals = tuple(map(lambda x: tuple(map(int, x.split("-"))), data))

smaller_intervals_within_bigger = itertools.starmap(
    lambda a, b, x, y: is_sorted((a, x, y, b)) or is_sorted((x, a, b, y)), intervals
)

# First puzzle answer
print(len(tuple(filter(bool, smaller_intervals_within_bigger))))

have_overlaps = itertools.starmap(
    lambda a, b, x, y: set(range(a, b + 1)) & set(range(x, y + 1)), intervals
)

# Second puzzle answer
print(len(tuple(filter(len, have_overlaps))))
