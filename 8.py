from __future__ import annotations

from functools import reduce
from itertools import chain, takewhile

from utils import read_trimmed

f = __file__.replace("py", "txt")


def parse(f) -> list[list[int]]:
    return [[int(c) for c in r] for r in read_trimmed(f)]


def q1(grid):
    visible = set()
    length = len(grid)
    width = len(grid[0])

    biggest = None
    for i in range(length):
        biggest = None
        for j in range(width):
            n = grid[i][j]
            if biggest is None or n > biggest:
                visible.add((i, j))
                biggest = n
    biggest = None
    for i in range(length):
        biggest = None
        for j in range(width - 1, -1, -1):
            n = grid[i][j]
            if biggest is None or n > biggest:
                visible.add((i, j))
                biggest = n
    biggest = None
    for j in range(width):
        biggest = None
        for i in range(length):
            n = grid[i][j]
            if biggest is None or n > biggest:
                visible.add((i, j))
                biggest = n
    biggest = None
    for j in range(width):
        biggest = None
        for i in range(length - 1, -1, -1):
            n = grid[i][j]
            if biggest is None or n > biggest:
                visible.add((i, j))
                biggest = n
    return len(visible)


def q2(grid):
    length = len(grid)
    width = len(grid[0])

    biggest = None
    for i in range(1, length - 1):
        for j in range(1, width - 1):
            n = grid[i][j]
            visibility = reduce(
                lambda x, y: x * y,
                [
                    1 + len([*takewhile(lambda i_0: grid[i_0][j] < n, range(i - 1, 0, -1))]),
                    1 + len([*takewhile(lambda i_0: grid[i_0][j] < n, range(i + 1, length - 1))]),
                    1 + len([*takewhile(lambda j_0: grid[i][j_0] < n, range(j - 1, 0, -1))]),
                    1 + len([*takewhile(lambda j_0: grid[i][j_0] < n, range(j + 1, width - 1))]),
                ],
            )
            if biggest is None or visibility > biggest:
                biggest = visibility

    return biggest


def main():
    print(q1(parse(f)))
    print(q2(parse(f)))


if __name__ == "__main__":
    main()
