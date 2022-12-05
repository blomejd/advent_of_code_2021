from pathlib import Path
from typing import Iterator
from utils import get_neighbors_n_dimensional, read_trimmed
from collections import deque, defaultdict, namedtuple
from statistics import median


class DictLike:
    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        setattr(self, key, value)


class Point(DictLike):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def fold(self, axis, line):
        if self[axis] > line:
            self[axis] = 2 * line - self[axis]
        return self


def q1(dots, folds):
    axis, line = folds[0]
    for dot in dots.copy():
        if axis == "x":
            if dot.x > line:
                dots.remove(dot)
                dots.add(Point(2 * line - dot.x, dot.y))
    return len(dots)


def print_dots(dots):
    x_max = max(dot.x for dot in dots)
    y_max = max(dot.y for dot in dots)
    grid = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]
    for dot in dots:
        grid[dot.y][dot.x] = "*"
    for row in grid:
        print("".join(row))


def q2(dots, folds):
    for axis, line in folds:
        # If edited in place, duplicates aren't removed *shrug*
        dots = {d.fold(axis, line) for d in dots}
    print_dots(dots)
    return len(dots)


def parse_dots(values):
    for v in values:
        dot = v.split(",")
        if len(dot) == 2:
            yield Point(int(dot[0]), int(dot[1]))


def parse_folds(values):
    for v in values:
        if len(v.split(" ")) == 3:
            fold = v.split(" ")[2]
            yield fold.split("=")[0], int(fold.split("=")[1])


def main():
    filename = "./13.txt"
    values = read_trimmed(filename)
    dots = set(parse_dots(values))
    folds = [*parse_folds(values)]
    print(q1(dots, folds))

    values = read_trimmed(filename)
    dots = set(parse_dots(values))
    folds = [*parse_folds(values)]
    print(q2(dots, folds))


if __name__ == "__main__":
    main()
