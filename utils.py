from pathlib import Path
from typing import List


def read_lines(filename: str) -> List[str]:
    with Path(filename).open("r", encoding="utf-8") as f:
        return [l for l in f]


def read_trimmed(filename: str) -> List[str]:
    return [l.strip() for l in read_lines(filename)]


def read_ints(filename: str) -> List[int]:
    return [int(l) for l in read_trimmed(filename)]


def read_delimited(filename: str, delimiter: str) -> List[str]:
    return [l.split(delimiter) for l in read_trimmed(filename)]


def get_neighbor_coords(x, y, grid):
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


def get_neighbors(x, y, grid):
    return [grid[y_n][x_n] for x_n, y_n in get_neighbor_coords(x, y, grid)]


def iter_coords(grid):
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            yield x, y
