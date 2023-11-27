from __future__ import annotations

import math
from collections import deque
from functools import cmp_to_key, reduce
from heapq import heapify
from itertools import chain, pairwise, product, takewhile


from utils import Point, iter_coords, read_trimmed, get_neighbor_coords

f = __file__.replace("py", "txt")


def parse(f) -> list[tuple[int, int, int]]:
    return [eval(l) for l in read_trimmed(f)]


def q1(lines: list[tuple[int,int, int]]):
    points = set(lines)
    for p in points:



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
