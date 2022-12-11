from __future__ import annotations

from collections import deque
from functools import reduce
from itertools import chain, takewhile

from utils import read_trimmed

f = __file__.replace("py", "txt")

to_one = lambda n: 0 if n == 0 else (1 if n > 0 else -1)


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def add(self, p: Point):
        self.x += p.x
        self.y += p.y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def dir_to(self, p: Point):
        d_x = p.x - self.x
        d_y = p.y - self.y
        if abs(d_x) <= 1 and abs(d_y) <= 1:
            return Point(0, 0)
        return Point(to_one(d_x), to_one(d_y))


dir_map = {
    "U": Point(0, 1),
    "D": Point(0, -1),
    "L": Point(-1, 0),
    "R": Point(1, 0),
}


def parse(f) -> list[tuple[str, int]]:
    g = (l.split(" ") for l in read_trimmed(f))
    parse_arg = lambda d: int(d[1]) if len(d) > 1 else 0
    return [(d[0], parse_arg(d)) for d in g]


def q1(commands):
    score = lambda i, x: i * x if (i - 20) % 40 == 0 else 0
    i, x, total = 1, 1, 0
    for (c, n) in commands:
        total += score(i, x)
        i += 1
        if c == "addx":
            total += score(i, x)
            i += 1
            x += n
    return total


def q2(commands):
    pixel = lambda i, x: "#" if abs(x - i % 40) <= 1 else " "
    i, x = 0, 1
    output = list("." for _ in range(240))
    for (c, n) in commands:
        output[i] = pixel(i, x)
        i += 1
        if c == "addx":
            output[i] = pixel(i, x)
            i += 1
            x += n
    return "\n".join("".join(output[k : k + 40]) for k in range(0, 240, 40))


def main():
    print(q1(parse(f)))
    print(q2(parse(f)))


if __name__ == "__main__":
    main()
