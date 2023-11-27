from __future__ import annotations

import math
from collections import deque
from functools import cmp_to_key, reduce
from heapq import heapify
from itertools import chain, pairwise, product, takewhile

from utils import Point, get_neighbor_coords_n_dimensional, iter_coords, read_trimmed

f = __file__.replace("py", "txt")


def parse(f) -> list[tuple[int, int, int]]:
    return [eval(l) for l in read_trimmed(f)]


def get_neighbors(p):
    return get_neighbor_coords_n_dimensional(None, p, diagonal=False, allowNegatives=True)


def q1(lines: list[tuple[int, int, int]]):
    points = set(lines)
    return sum(sum(1 for c in get_neighbors(p) if c not in points) for p in lines)


def q2(lines):
    # print(sorted(lines))
    points = set(lines)
    x_avg = sum(x for x, y, z in lines) / len(lines)
    y_avg = sum(y for x, y, z in lines) / len(lines)
    z_avg = sum(z for x, y, z in lines) / len(lines)
    core = (int(x_avg), int(y_avg), int(z_avg))
    # core = (2, 2, 5)

    to_search = set(n for n in get_neighbors(core) if n not in points)
    searched = set([core])
    while to_search:
        p = to_search.pop()
        searched.add(p)
        to_search.update(n for n in get_neighbors(p) if n not in (searched | points))
    # print(searched)
    total = sum(sum(1 for n in get_neighbors(p) if n not in points) for p in lines)
    inner = sum(sum(1 for n in get_neighbors(p) if n not in searched) for p in searched)
    return total - inner


def main():
    # for left, right in parse(f):
    #     print(left, right)
    print(q1(parse(f)))
    print(q2(parse(f)))


if __name__ == "__main__":
    main()
