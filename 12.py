from __future__ import annotations

import math
from collections import deque
from functools import reduce
from itertools import chain, takewhile

from utils import (Point, get_neighbor_coords_n_dimensional, get_neighbors,
                   get_orthogonal_neighbors, iter_coords, read_trimmed)

f = __file__.replace("py", "txt")


def fake_ord(c):
    if c == "E":
        return 26
    if c == "S":
        return 1
    if c == c.lower():
        return ord(c) - 96
    return ord(c) - 64 + 26


print(fake_ord("a"))


def parse(f) -> list[list[int]]:
    return [[fake_ord(c) for c in l] for l in read_trimmed(f)]


def find_start():
    grid = [[c for c in l] for l in read_trimmed(f)]
    for i, j in iter_coords(grid):
        if grid[j][i] == "S":
            return i, j


def find_end():
    grid = [[c for c in l] for l in read_trimmed(f)]
    for i, j in iter_coords(grid):
        if grid[j][i] == "E":
            return i, j


end = find_end()

def helper(grid, start):
    # print(list(get_neighbor_coords_n_dimensional(grid, (0, 7), diagonal=False)))
    visited = {start}
    boundary = deque(
        (c_x, c_y)
        for (c_y, c_x) in get_neighbor_coords_n_dimensional(
            grid, (start[1], start[0]), diagonal=False
        )
    )
    steps = 1
    while boundary:
        next_boundary = set()
        for x, y in boundary:
            if (x, y) == end:
                return steps
            neighbors = get_neighbor_coords_n_dimensional(grid, (y, x), diagonal=False)
            next_boundary.update((X, Y) for (Y, X) in neighbors if grid[Y][X] - grid[y][x] <= 1)
        visited.update(boundary)
        boundary = next_boundary - visited
        steps += 1
    return math.inf


def q1_a(grid):
    start = find_start()
    return helper(grid, start)


def q2(grid):
    starts = [(x, y) for x, y in iter_coords(grid) if grid[y][x] == 1]
    # starts = [find_start()]
    global_mins = {}
    result = math.inf
    for start in starts:
        global_mins[start] = 0
        # print(list(get_neighbor_coords_n_dimensional(grid, (0, 7), diagonal=False)))
        visited = {start}
        boundary = deque(
            (c_x, c_y)
            for (c_y, c_x) in get_neighbor_coords_n_dimensional(
                grid, (start[1], start[0]), diagonal=False
            )
            if grid[c_y][c_x] <= 2
        )
        steps = 1
        while boundary:
            if steps >= result:
                break
            next_boundary = set()
            for x, y in boundary:
                if (x, y) == end:
                    if steps < result:
                        result = steps
                    next_boundary = set()
                    break
                # if global_mins.get((x, y), math.inf) < steps:
                #     continue
                global_mins[(x, y)] = steps
                neighbors = get_neighbor_coords_n_dimensional(grid, (y, x), diagonal=False)
                next_boundary.update((X, Y) for (Y, X) in neighbors if grid[Y][X] - grid[y][x] <= 1)
            visited.update(boundary)
            boundary = next_boundary - visited
            steps += 1
    return result


def main():
    # print(parse(f))
    print(q1_a(parse(f)))
    print(q2(parse(f)))


if __name__ == "__main__":
    main()
