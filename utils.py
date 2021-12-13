from pathlib import Path
from typing import List
from itertools import product


def read_lines(filename: str) -> List[str]:
    with Path(filename).open("r", encoding="utf-8") as f:
        return [l for l in f]


def read_trimmed(filename: str) -> List[str]:
    return [l.strip() for l in read_lines(filename)]


def read_ints(filename: str) -> List[int]:
    return [int(l) for l in read_trimmed(filename)]


def read_int_rows(filename: str):
    return [[int(c) for c in row] for row in read_trimmed(filename)]


def read_delimited(filename: str, delimiter: str) -> List[str]:
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


def get_neighbor_coords_n_dimensional(grid, coord, orthogonal=True, diagonal=True):
    dimensions = get_dimensions(grid)
    deltas = list(product(*[[1, 0, -1] for _ in dimensions]))
    if orthogonal and diagonal:
        deltas = [d for d in deltas if any(n != 0 for n in d)]
    elif orthogonal:
        deltas = [d for d in deltas if one(n != 0 for n in d)]
    elif diagonal:
        deltas = [d for d in deltas if all(n != 0 for n in d)]
    for delta in deltas:
        # yield tuple(coord[i] + delta[i] for i in range(dimensions))
        if all(0 <= c + d < dim for dim, c, d in zip(dimensions, coord, delta)):
            yield tuple(c + d for c, d in zip(coord, delta))


def get_neighbors_n_dimensional(grid, coord, orthogonal=True, diagonal=True):
    for neighbor_coord in get_neighbor_coords_n_dimensional(grid, coord, orthogonal, diagonal):
        needle = grid
        for c in neighbor_coord:
            needle = needle[c]
        yield needle
