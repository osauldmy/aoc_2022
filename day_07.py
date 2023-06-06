#!/usr/bin/env python3
import collections
import functools
import pathlib


with open(pathlib.Path(__file__).parent / "input" / "day_07.txt") as f:
    data = f.read().strip("\n").split("\n")

file_sizes, tree = {}, collections.defaultdict(set)
current_path = pathlib.Path(".")
for line in data:
    match line.split(" "):
        case "$", "cd", path:
            current_path = (current_path / path).resolve()
        case "$", "ls":
            pass
        case "dir", dir_name:
            tree[current_path].add(dir_name)
        case file_size, file_name:
            tree[current_path].add(file_name)
            file_sizes[(current_path / file_name).resolve()] = int(file_size)


@functools.cache
def calculate_dir_sizes(path: pathlib.Path) -> int:
    if path not in tree:  # keys are directories, so this checks if path is a file
        return file_sizes[path]
    return sum(
        calculate_dir_sizes((path / sub_path).resolve()) for sub_path in tree[path]
    )


dir_sizes = tuple(map(calculate_dir_sizes, tree))

# First puzzle answer
print(sum(filter(lambda x: x <= 100_000, dir_sizes)))

# Second puzzle answer
already_free = 70_000_000 - max(dir_sizes)
print(min(filter(lambda x: already_free + x >= 30_000_000, dir_sizes)))
