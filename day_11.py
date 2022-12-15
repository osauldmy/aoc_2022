#!/bin/env python3
from __future__ import annotations

import collections
import dataclasses
import operator
import pathlib
import re
import typing

if typing.TYPE_CHECKING:
    from typing import Callable, Deque


with open(pathlib.Path(__file__).parent / "input" / "day_11.txt") as f:
    data = f.read().strip("\n")


@dataclasses.dataclass
class Monkey:
    items: Deque[int]
    operation: Callable[[int], int]
    divisible_by: int
    throw_to: tuple[int, int]
    inspected: int = 0

    @classmethod
    def parse(cls, raw: tuple[str, str, str, str, str]) -> Monkey:
        items = collections.deque(map(int, raw[0].split(", ")))
        a, _operator, b = raw[1].split(" ")
        operation = lambda n: {"+": operator.add, "*": operator.mul}[_operator](
            n if a == "old" else int(a), n if b == "old" else int(b)
        )
        by, yes, no = map(int, raw[2:])
        return cls(items, operation, by, (no, yes))


pattern = r"""
Monkey \d+:
  Starting items: ([\d+, ]*\d+)
  Operation: new = (.*)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)
"""

monkeys = tuple(map(Monkey.parse, re.findall(pattern.strip("\n"), data)))

for _ in range(20):
    for monkey in monkeys:
        while monkey.items:
            x = monkey.operation(monkey.items.popleft()) // 3
            monkeys[monkey.throw_to[x % monkey.divisible_by == 0]].items.append(x)
            monkey.inspected += 1

# First puzzle answer
print(operator.mul(*sorted(monkey.inspected for monkey in monkeys)[-2:]))

# Second puzzle answer
print("todo")
