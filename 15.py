from __future__ import annotations

import math
from collections import deque
from functools import cmp_to_key, reduce
from heapq import heapify
from itertools import chain, pairwise, product, takewhile

from utils import Point, iter_coords, read_trimmed

f = __file__.replace("py", "txt")


def parse(f) -> list[tuple[Point, Point, int]]:
    g = [[int(d) for d in l.split(" ")] for l in read_trimmed(f)]
    g2 = ((Point(x, y), Point(x_0, y_0)) for x, y, x_0, y_0 in g)
    return [(s, b, Point.manhattan(s, b)) for s, b in g2]


def q1(lines: list[tuple[Point, Point, int]]):
    x_min = min(s.x - d for s, b, d in lines)
    x_max = max(s.x + d for s, b, d in lines)
    y = 2_000_000
    lines = [(s, b, d) for s, b, d in lines if s.y + d >= y >= s.y - d]
    return len(
        {
            x
            for x in range(x_min, x_max + 1)
            if any(Point.manhattan(Point(x, y), s) <= d and Point(x, y) != b for s, b, d in lines)
        }
    )


TUNING = 4_000_000


def q2(lines):
    n = 4_000_000
    lines = [(s, d) for s, _, d in lines]
    for y in range(n):
        if y % 10_000 == 0:
            print(y)
        # diffs = (d - abs(s.y - y) for s, d in lines if s.y + d >= y >= s.y - d)
        # ranges = [
        #     (s.x - d + abs(s.y - y), s.x + d - abs(s.y - y)) for diff, (s, d) in zip(diffs, lines)
        # ]
        ranges = [(s.x - d + abs(s.y - y), s.x + d - abs(s.y - y)) for s, d in lines]
        ranges.sort()
        r = ranges[0]
        for left, right in ranges:
            if r[1] < (left - 1) and r[1] < n:
                return (r[1] + 1) * TUNING + y
            r = (min(r[0], left), max(r[1], right))


def main():
    # for left, right in parse(f):
    #     print(left, right)
    # print(q1(parse(f)))
    print(q2(parse(f)))


if __name__ == "__main__":
    main()
