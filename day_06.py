#!/bin/env python3
import pathlib

import more_itertools

with open(pathlib.Path(__file__).parent / "day_06.input.txt") as f:
    data = f.read().strip("\n")

for index, window in enumerate(more_itertools.sliding_window(data, 4)):
    if len(set(window)) == 4:
        # First puzzle answer
        print(4 + index)
        break

for index, window in enumerate(more_itertools.sliding_window(data, 14)):
    if len(set(window)) == 14:
        # Second puzzle answer
        print(14 + index)
        break
