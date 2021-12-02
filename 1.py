from pathlib import Path
from typing import Iterator
from utils import read_ints


def q1(values):
    print(sum(v < values[i + 1] for i, v in enumerate(values[:-1])))


def q2(values):
    print(sum(v < values[i + 3] for i, v in enumerate(values[:-3])))


def main():
    values = read_ints("./1.txt")
    q1(values)
    q2(values)


if __name__ == "__main__":
    main()
