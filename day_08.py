#!/bin/env python3
from __future__ import annotations

import functools
import operator
import pathlib
import typing

if typing.TYPE_CHECKING:
    from typing import Callable, Iterable, Iterator

    T = typing.TypeVar("T")


def takewhile_with_last(
    predicate: Callable[[T], bool], iterable: Iterable[T]
) -> Iterator[T]:
    for value in iterable:
        yield value
        if not predicate(value):
            return


with open(pathlib.Path(__file__).parent / "input" / "day_08.txt") as f:
    data = f.read().strip("\n").split("\n")

forest = tuple(map(lambda x: tuple(map(int, x)), data))
col = lambda i: tuple(_[i] for _ in forest)

count = 0
for i, row in enumerate(forest[1:-1], 1):
    for j, tree in enumerate(row[1:-1], 1):
        views = col(j)[:i], col(j)[i + 1 :][::-1], row[:j], row[j + 1 :][::-1]
        count += any(map(lambda x: max(x) < tree, views))

# First puzzle answer
print(len(forest) * 2 + len(forest[0]) * 2 - 4 + count)

scenic_scores = set()
for i, row in enumerate(forest[1:-1], 1):
    for j, tree in enumerate(row[1:-1], 1):
        views = col(j)[:i][::-1], col(j)[i + 1 :], row[:j][::-1], row[j + 1 :]
        x = map(
            lambda view: len(tuple(takewhile_with_last(lambda x: x < tree, view))),
            views,
        )
        scenic_scores.add(functools.reduce(operator.mul, x))

# Second puzzle answer
print(max(scenic_scores))
