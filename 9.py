from __future__ import annotations

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
    g = (r.split(" ") for r in read_trimmed(f))
    return [(d, int(n)) for [d, n] in g]


def q1(commands):
    head = Point(0, 0)
    tail = Point(0, 0)
    visitied = set([str(tail)])
    for (d, n) in commands:
        for _ in range(n):
            head.add(dir_map[d])
            tail.add(tail.dir_to(head))
            visitied.add(str(tail))
    return len(visitied)


def q2(commands):
    rope = [Point(0, 0) for _ in range(9)]
    head = Point(0, 0)
    tail = rope[-1]
    visitied = set([str(tail)])
    for (d, n) in commands:
        for _ in range(n):
            head.add(dir_map[d])
            prev = head
            for knot in rope:
                knot.add(knot.dir_to(prev))
                prev = knot
            visitied.add(str(tail))
    return len(visitied)

    return 0


def main():
    print(q1(parse(f)))
    print(q2(parse(f)))


if __name__ == "__main__":
    main()
