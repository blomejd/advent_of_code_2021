from math import prod

from utils import get_orthogonal_coords, get_orthogonal_neighbors, iter_coords, read_trimmed


def iter_basins(grid):
    for x, y in iter_coords(grid):
        neighbors = get_orthogonal_neighbors(x, y, grid)
        if all(grid[y][x] < n for n in neighbors):
            yield x, y


def q1(grid):
    return sum(grid[y][x] + 1 for x, y in iter_basins(grid))


def q2(grid):
    basins = {(x, y): set() for x, y in iter_basins(grid)}

    for x, y in basins:
        to_search = get_orthogonal_coords(x, y, grid)
        while to_search:
            x_n, y_n = to_search.pop()
            if grid[y_n][x_n] == 9 or (x_n, y_n) in basins[(x, y)]:
                continue
            basins[(x, y)].add((x_n, y_n))
            to_search |= get_orthogonal_coords(x_n, y_n, grid)

    lens = sorted((len(v) for v in basins.values()), reverse=True)
    return prod(lens[:3])


def main():
    values = [[int(c) for c in row] for row in read_trimmed("9.txt")]
    print(q1(values))
    print(q2(values))


if __name__ == "__main__":
    main()
