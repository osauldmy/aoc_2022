#!/bin/env python3
from __future__ import annotations

import collections
import pathlib
import typing

if typing.TYPE_CHECKING:
    from typing import Iterator

    Grid = tuple[list[str], ...]
    Point = tuple[int, int]

with open(pathlib.Path(__file__).parent / "input" / "day_12.txt") as f:
    data = f.read().strip("\n")


def find_point(grid: Grid, string: str) -> Iterator[Point]:
    for y, _ in filter(lambda x: x[1], enumerate(string in row for row in grid)):
        for x, value in enumerate(grid[y]):
            if value == string:
                yield y, x


def get_path_length(path: dict[Point, Point], point: Point) -> int:
    """
    0 indicates there was no path from start to end
    """
    if not (predecessor := path.get(point)):
        return 0
    return get_path_length(path, predecessor) + 1


def constrained_bfs(grid: Grid, start: Point, end: Point) -> dict[Point, Point]:
    path, opened, closed = dict(), set(), set()
    Q = collections.deque((start,))
    while Q:
        y, x = Q.popleft()
        if (y, x) == end:
            break

        for neighbor in (
            (y + 1, x),
            (y - 1, x),
            (y, x + 1),
            (y, x - 1),
        ):
            n_y, n_x = neighbor
            if neighbor in opened or neighbor in closed:
                continue

            if n_y < 0 or n_x < 0 or n_y >= len(grid) or n_x >= len(grid[0]):
                continue

            if ord(grid[n_y][n_x]) - ord(grid[y][x]) > 1:  # elevation constraint
                continue

            Q.append(neighbor)
            opened.add(neighbor)
            path[neighbor] = (y, x)
        closed.add((y, x))
    return path


if __name__ == "__main__":
    grid: Grid = tuple(map(list, data.split("\n")))
    start, end = next(find_point(grid, "S")), next(find_point(grid, "E"))
    grid[start[0]][start[1]] = "a"  # resetting S elevation to a
    grid[end[0]][end[1]] = "z"  # resetting E elevation to z

    # First puzzle answer
    print(get_path_length(constrained_bfs(grid, start, end), end))

    # Second puzzle answer
    lengths = (
        get_path_length(constrained_bfs(grid, s, end), end)
        for s in find_point(grid, "a")
    )
    print(min(filter(bool, lengths)))
