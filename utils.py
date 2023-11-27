from __future__ import annotations

import math
from fractions import Fraction
from itertools import product, zip_longest
from pathlib import Path
from typing import List


def read_lines(filename: str) -> List[str]:
    with Path(filename).open("r", encoding="utf-8") as f:
        return [l for l in f]


def read_trimmed(filename: str) -> List[str]:
    return [l.strip() for l in read_lines(filename)]


def read_ints(filename: str) -> List[int]:
    return [int(l) for l in read_trimmed(filename)]


def read_int_rows(filename: str):
    return [[int(c) for c in row] for row in read_trimmed(filename)]


def read_delimited(filename: str, delimiter: str) -> List[List[str]]:
    return [l.split(delimiter) for l in read_trimmed(filename)]


def get_orthogonal_coords(x, y, grid):
    width = len(grid[0])
    height = len(grid)
    neighbors = set()
    if x > 0:
        neighbors.add((x - 1, y))
    if x < width - 1:
        neighbors.add((x + 1, y))
    if y > 0:
        neighbors.add((x, y - 1))
    if y < height - 1:
        neighbors.add((x, y + 1))
    return neighbors


def get_neighbor_coords(x, y, grid):
    width = len(grid[0])
    height = len(grid)
    neighbors = set()
    for x_d, y_d in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
        x_n = x + x_d
        y_n = y + y_d
        if 0 <= x_n < width and 0 <= y_n < height:
            neighbors.add((x_n, y_n))
    return neighbors


def get_neighbors(x, y, grid):
    return [grid[y_n][x_n] for x_n, y_n in get_neighbor_coords(x, y, grid)]


def get_orthogonal_neighbors(x, y, grid):
    return [grid[y_n][x_n] for x_n, y_n in get_orthogonal_coords(x, y, grid)]


def iter_coords(grid):
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            yield x, y


def get_dimensions(grid):
    dimensions = []
    grid_copy = grid
    while isinstance(grid_copy, list):
        dimensions.append(len(grid_copy))
        if grid_copy:
            grid_copy = grid_copy[0]
        else:
            break
    return dimensions


def one(iterable):
    return len([v for v in iterable if v]) == 1


def get_neighbor_coords_n_dimensional(
    grid,
    coord,
    orthogonal=True,
    diagonal=True,
    allowNegatives=False,
):
    dimensions = get_dimensions(grid) if grid else [math.inf] * len(coord)
    deltas = list(product(*[[1, 0, -1] for _ in dimensions]))
    if orthogonal and diagonal:
        deltas = [d for d in deltas if any(n != 0 for n in d)]
    elif orthogonal:
        deltas = [d for d in deltas if one(n != 0 for n in d)]
    elif diagonal:
        deltas = [d for d in deltas if all(n != 0 for n in d)]
    lower_bound = -math.inf if allowNegatives else 0
    for delta in deltas:
        if all(lower_bound <= c + d < dim for dim, c, d in zip(dimensions, coord, delta)):
            yield tuple(c + d for c, d in zip(coord, delta))


def get_neighbors_n_dimensional(grid, coord, orthogonal=True, diagonal=True):
    for neighbor_coord in get_neighbor_coords_n_dimensional(grid, coord, orthogonal, diagonal):
        needle = grid
        for c in reversed(neighbor_coord):
            needle = needle[c]
        yield needle


# Stolen from https://docs.python.org/3/library/itertools.html#itertools-recipes
def grouper(iterable, n, *, incomplete="fill", fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == "fill":
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == "strict":
        return zip(*args, strict=True)
    if incomplete == "ignore":
        return zip(*args)
    else:
        raise ValueError("Expected fill, strict, or ignore")


class Point(tuple):
    def __init__(self, x, y) -> None:
        # super().__init__([x, y])
        self.x = x
        self.y = y

    def __new__(cls, x, y):
        return super().__new__(cls, tuple([x, y]))

    def add(self, p: Point):
        self.x += p.x
        self.y += p.y

    def translate(self, x, y):
        return Point(self.x + x, self.y + y)

    # def __repr__(self) -> str:
    #     return f"({self.x}, {self.y})"

    # def __hash__(self) -> int:
    #     return hash((self.x, self.y))

    def dir_to(self, p: Point):
        d_x = p.x - self.x
        d_y = p.y - self.y
        if abs(d_x) <= 1 and abs(d_y) <= 1:
            return Point(0, 0)
        return Point(self.to_one(d_x), self.to_one(d_y))

    @staticmethod
    def to_one(n):
        if n == 0:
            return 0
        return 1 if n > 0 else -1

    def points_between(self, other: Point) -> list[Point]:
        d_x = other.x - self.x
        d_y = other.y - self.y
        if d_x == 0:
            bottom, top = (self, other) if self.y <= other.y else (other, self)
            return [Point(self.x, y_0) for y_0 in range(bottom.y, top.y + 1, 1)]
        left, right = (self, other) if self.x <= other.x else (other, self)
        if d_y == 0:
            return [Point(x_0, self.y) for x_0 in range(left.x, right.x + 1, 1)]
        f = Fraction(d_y, d_x)
        left, right = (self, other) if self.x <= other.x else (other, self)
        y_mod = 1 if f.numerator > 0 else -1
        g_x = range(left.x, right.x + 1, f.denominator)
        g_y = range(left.y, right.y + y_mod, f.numerator)
        return [Point(*c) for c in zip(g_x, g_y)]

    @staticmethod
    def between(first: Point, last: Point) -> list[Point]:
        d_x = first.x - last.x
        d_y = first.y - last.y
        if d_x == 0:
            bottom, top = (last, first) if last.y <= first.y else (first, last)
            return [Point(last.x, y_0) for y_0 in range(bottom.y, top.y + 1, 1)]
        left, right = (last, first) if last.x <= first.x else (first, last)
        if d_y == 0:
            return [Point(x_0, last.y) for x_0 in range(left.x, right.x + 1, 1)]
        f = Fraction(d_y, d_x)
        left, right = (last, first) if last.x <= first.x else (first, last)
        y_mod = 1 if f.numerator > 0 else -1
        g_x = range(left.x, right.x + 1, f.denominator)
        g_y = range(left.y, right.y + y_mod, f.numerator)
        return [Point(*c) for c in zip(g_x, g_y)]

    @staticmethod
    def manhattan(first: Point, last: Point) -> int:
        return abs(first.x - last.x) + abs(first.y - last.y)


dir_map = {
    "U": Point(0, 1),
    "D": Point(0, -1),
    "L": Point(-1, 0),
    "R": Point(1, 0),
}
