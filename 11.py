from __future__ import annotations

from collections import defaultdict, deque
from functools import reduce
from itertools import chain, takewhile

from utils import read_trimmed

f = __file__.replace("py", "txt")

monkeys: list[Monkey] = []


class Monkey:
    def __init__(self, items, operation, test, i_true, i_false) -> None:
        self.inspections = 0
        self.items = deque(items)
        self.operation = operation
        self.test = test
        self.i_true = i_true
        self.i_false = i_false

    def turn_0(self):
        while self.items:
            item = self.operation(self.items.popleft()) // 3
            self.inspections += 1
            receiver_i = self.i_true if self.test(item) else self.i_false
            monkeys[receiver_i].items.append(item)

    def turn(self):
        self.inspections += len(self.items)
        while self.items:
            item = self.operation(self.items.popleft()) % 9699690
            receiver_i = self.i_true if self.test(item) else self.i_false
            monkeys[receiver_i].items.append(item)


monkeys = [
    Monkey(
        items=[92, 73, 86, 83, 65, 51, 55, 93],
        operation=lambda x: x * 5,
        test=lambda x: x % 11 == 0,
        i_true=3,
        i_false=4,
    ),
    Monkey(
        items=[99, 67, 62, 61, 59, 98],
        operation=lambda x: x * x,
        test=lambda x: x % 2 == 0,
        i_true=6,
        i_false=7,
    ),
    Monkey(
        items=[81, 89, 56, 61, 99],
        operation=lambda x: x * 7,
        test=lambda x: x % 5 == 0,
        i_true=1,
        i_false=5,
    ),
    Monkey(
        items=[97, 74, 68],
        operation=lambda x: x + 1,
        test=lambda x: x % 17 == 0,
        i_true=2,
        i_false=5,
    ),
    Monkey(
        items=[78, 73],
        operation=lambda x: x + 3,
        test=lambda x: x % 19 == 0,
        i_true=2,
        i_false=3,
    ),
    Monkey(
        items=[50],
        operation=lambda x: x + 5,
        test=lambda x: x % 7 == 0,
        i_true=1,
        i_false=6,
    ),
    Monkey(
        items=[95, 88, 53, 75],
        operation=lambda x: x + 8,
        test=lambda x: x % 3 == 0,
        i_true=0,
        i_false=7,
    ),
    Monkey(
        items=[50, 77, 98, 85, 94, 56, 89],
        operation=lambda x: x + 2,
        test=lambda x: x % 13 == 0,
        i_true=4,
        i_false=0,
    ),
]


def q1():
    for _ in range(20):
        for monkey in monkeys:
            monkey.turn()
    counts = sorted(m.inspections for m in monkeys)
    return counts[-1] * counts[-2]


def q2():
    for _ in range(10000):
        for monkey in monkeys:
            monkey.turn()
    counts = sorted(m.inspections for m in monkeys)
    return counts[-1] * counts[-2]


def main():
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
