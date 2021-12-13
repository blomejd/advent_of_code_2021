from pathlib import Path
from typing import Iterator
from utils import get_neighbors_n_dimensional, get_neighbor_coords_n_dimensional, get_dimensions
from collections import deque
from statistics import median


def main():
    assert get_dimensions([]) == [0]
    assert get_dimensions([1]) == [1]
    assert get_dimensions([[]]) == [1, 0]
    assert get_dimensions([[1], [1]]) == [2, 1]
    assert get_dimensions([[[]]]) == [1, 1, 0]

    print(list(get_neighbor_coords_n_dimensional([[4, 5], [6, 7]], (0, 0))))


if __name__ == "__main__":
    main()
