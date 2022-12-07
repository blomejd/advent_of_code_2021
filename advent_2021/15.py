from collections import defaultdict, deque, namedtuple
from math import inf
from statistics import median
from typing import Iterator

from utils import get_neighbors_n_dimensional, iter_coords, read_trimmed


class Path:
    def __init__(self, x, y, steps, total):
        self.x, self.y = x, y
        self.steps, self.total = steps, total

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}), {self.total}"


def q1(grid):
    grid[0][0] = 0
    paths = [[Path(x, y, [], inf) for x in range(len(grid[0]))] for y in range(len(grid))]
    paths[0][0] = Path(0, 0, [], 0)

    p = Path(0, 0, [], 0)
    to_search = {p}
    while to_search:
        p = to_search.pop()
        for p_n in get_neighbors_n_dimensional(paths, (p.x, p.y), diagonal=False):
            if p.total + grid[p_n.y][p_n.x] < p_n.total:
                to_search.add(p_n)
                p_n.total = p.total + grid[p_n.y][p_n.x]
                p_n.steps = [*p.steps, p_n]

    # p = Path(0, 0, [], 0)
    # to_search = {(p.x, p.y)}
    # while to_search:
    #     x, y = to_search.pop()
    #     p = paths[y][x]
    #     for p_n in get_neighbors_n_dimensional(paths, (x, y), diagonal=False):
    #         if p.total + grid[p_n.y][p_n.x] < p_n.total:
    #             to_search.add((p_n.x, p_n.y))
    #             p_n.total = p.total + grid[p_n.y][p_n.x]
    return paths[-1][-1]


def print_grid(grid):
    return "\n".join(["".join([str(c) for c in row]) for row in grid])


def q2(grid):
    for y, row in enumerate(grid[:]):
        row = row[:]
        for i in range(1, 5):
            grid[y].extend(((x + i - 1) % 9) + 1 for x in row)

    grid_c = grid[:]
    for i in range(1, 5):
        for row in grid_c:
            grid.append([((x + i - 1) % 9) + 1 for x in row])

    return q1(grid)


def parse_values():
    filename = "./15.txt"
    values = read_trimmed(filename)
    return [[int(c) for c in v] for v in values]


def main():
    print(q1(parse_values()))
    print(q2(parse_values()))


if __name__ == "__main__":
    main()
