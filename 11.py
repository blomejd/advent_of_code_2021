from __future__ import annotations

from collections import deque
from functools import reduce
from itertools import chain, takewhile

from utils import read_trimmed

f = __file__.replace("py", "txt")


def parse(f) -> list[tuple[str, int]]:
    g = (l.split(" ") for l in read_trimmed(f))
    parse_arg = lambda d: int(d[1]) if len(d) > 1 else 0
    return [(d[0], parse_arg(d)) for d in g]


def q1(commands):
    return 0


def q2(commands):
    return 0


def main():
    print(q1(parse(f)))
    print(q2(parse(f)))


if __name__ == "__main__":
    main()
