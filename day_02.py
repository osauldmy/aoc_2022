#!/bin/env python3
from __future__ import annotations

import pathlib


with open(pathlib.Path(__file__).parent / "day_02.input.txt") as f:
    data = f.read()


def first(play: list[str]) -> int:
    opponent, you = map(int, play)
    # (1 - 2), (3 - 1), (2 - 3) each mod 3 result in 2 -> win
    # (2 - 1), (1 - 3), (3 - 2) each mod 3 result in 1 -> lose
    # (1 - 1), (2 - 2), (3 - 3) each mod 3 result in 0 -> tie
    score = (opponent - you) % 3
    return you + (3 if score == 0 else 6 if score == 2 else 0)


def second(play: list[str]) -> int:
    opponent, outcome = map(int, play)
    if outcome == 1:  # lose
        return 0 + (opponent - 1 if opponent in (2, 3) else 3)
    if outcome == 2:  # tie
        return 3 + opponent
    # if outcome == 3:  win
    return 6 + (opponent + 1 if opponent in (1, 2) else 1)


plays = tuple(
    map(
        str.split,
        data.translate(data.maketrans("AXBYCZ", "112233")).strip("\n").split("\n"),
    )
)

# First puzzle answer
print(sum(map(first, plays)))

# Second puzzle answer
print(sum(map(second, plays)))
