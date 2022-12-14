from __future__ import annotations

import math
from collections import deque
from functools import cmp_to_key, reduce
from itertools import chain, takewhile

from utils import (
    Point,
    get_neighbor_coords_n_dimensional,
    get_neighbors,
    get_orthogonal_neighbors,
    grouper,
    iter_coords,
    read_trimmed,
)

f = __file__.replace("py", "txt")


def parse(f) -> list[tuple]:
    g = grouper(read_trimmed(f), 3)
    return [(eval(l), eval(r)) for l, r, _ in g]


def list_compare(left, right):
    # print("list", left, right)
    g = list(zip(left, right))
    for l, r in g:
        c = packet_compare(l, r)
        if c != 0:
            return c
    if len(left) < len(right):
        return 1
    if len(right) < len(left):
        return -1
    return 0


def packet_compare(left, right):
    # print("packet", left, right)
    if type(left) is int and type(right) is int:
        if left < right:
            return 1
        if right < left:
            return -1
        return 0
    if type(left) is int:
        left = [left]
    if type(right) is int:
        right = [right]
    return list_compare(left, right)


def q1_a(packets):
    total = 0
    for i, (l, r) in enumerate(packets):
        # print()
        c = packet_compare(l, r)
        # print(i, c)
        if c == 1:
            total += i + 1
    return total


def q2(packets):
    d_2 = [[2]]
    d_6 = [[6]]
    packets = sorted([*chain(*packets, [d_2, d_6])], key=cmp_to_key(packet_compare))
    packets.reverse()
    return (packets.index(d_2) + 1) * (packets.index(d_6) + 1)


def main():
    # for left, right in parse(f):
    #     print(left, right)
    print(q1_a(parse(f)))
    print(q2(parse(f)))


if __name__ == "__main__":
    main()
