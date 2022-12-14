from __future__ import annotations

import math
from collections import deque
from functools import cmp_to_key, reduce
from itertools import chain, pairwise, takewhile

from utils import Point, iter_coords, read_trimmed

f = __file__.replace("py", "txt")


def parse(f) -> list[list[Point]]:
    return [[Point(*eval(chunk)) for chunk in l.split("->")] for l in read_trimmed(f)]


def q1(shapes: list[list[Point]]):
    line_g = (p.points_between(q) for s in shapes for p, q in pairwise(s))
    rocks = {*chain.from_iterable(line_g)}
    sand: set[Point] = set()
    lowest = max(r.y for r in rocks)

    while True:
        x, y = 500, 0
        while True:
            candidates = [Point(x, y + 1), Point(x - 1, y + 1), Point(x + 1, y + 1)]
            try:
                x, y = next(p for p in candidates if p not in sand and p not in rocks)
                if y > lowest:
                    return len(sand)
            except StopIteration:
                sand.add(Point(x, y))
                break
    return -1


def q2(shapes):
    line_g = (p.points_between(q) for s in shapes for p, q in pairwise(s))
    rocks = {*chain.from_iterable(line_g)}
    sand: set[Point] = set()
    lowest = max(r.y for r in rocks)

    while True:
        x, y = 500, 0
        while True:
            candidates = [Point(x, y + 1), Point(x - 1, y + 1), Point(x + 1, y + 1)]
            try:
                x, y = next(p for p in candidates if p not in sand and p not in rocks)
                if y == lowest + 1:
                    sand.add(Point(x, y))
                    break
            except StopIteration:
                sand.add(Point(x, y))
                break
        if (x, y) == (500, 0):
            return len(sand)
    return -1


def main():
    # for left, right in parse(f):
    #     print(left, right)
    # print(q1(parse(f)))
    print(q2(parse(f)))


if __name__ == "__main__":
    main()
