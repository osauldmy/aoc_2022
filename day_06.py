#!/bin/env python3
import pathlib

import more_itertools

with open(pathlib.Path(__file__).parent / "input" / "day_06.txt") as f:
    data = f.read().strip("\n")


def find_index(sequence: str, n: int) -> int:
    for index, window in enumerate(more_itertools.sliding_window(sequence, n)):
        if len(set(window)) == n:
            break
    return n + index


# First puzzle answer
print(find_index(data, 4))

# Second puzzle answer
print(find_index(data, 14))
