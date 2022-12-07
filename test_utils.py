from collections import deque
from pathlib import Path
from statistics import median
from typing import Iterator

from utils import get_dimensions, get_neighbor_coords_n_dimensional, get_neighbors_n_dimensional


def main():
    assert get_dimensions([]) == [0]
    assert get_dimensions([1]) == [1]
    assert get_dimensions([[]]) == [1, 0]
    assert get_dimensions([[1], [1]]) == [2, 1]
    assert get_dimensions([[[]]]) == [1, 1, 0]

    print(list(get_neighbor_coords_n_dimensional([[4, 5], [6, 7]], (0, 0))))


if __name__ == "__main__":
    main()
