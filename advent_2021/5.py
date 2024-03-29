import re
from collections import Counter
from itertools import chain

from utils import read_trimmed


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_points(self):
        if self.x1 == self.x2:
            xs = [self.x1] * (abs(self.y2 - self.y1) + 1)
        else:
            x_d = 1 if self.x1 < self.x2 else -1
            xs = range(self.x1, self.x2 + x_d, x_d)

        if self.y1 == self.y2:
            ys = [self.y1] * (abs(self.x2 - self.x1) + 1)
        else:
            y_d = 1 if self.y1 < self.y2 else -1
            ys = range(self.y1, self.y2 + y_d, y_d)
        return zip(xs, ys)


def parse_lines(values):
    values = [[int(n.strip()) for n in re.split("->|,", s)] for s in values]
    return [Line(*v) for v in values]


def count_values(lines):
    count = Counter(chain.from_iterable(l.get_points() for l in lines))
    return len([v for v in count.values() if v >= 2])


def q1(values):
    lines = parse_lines(values)
    lines = [l for l in lines if l.x1 == l.x2 or l.y1 == l.y2]
    return count_values(lines)


def q2(values):
    lines = parse_lines(values)
    return count_values(lines)


def main():
    values = list(read_trimmed("5.txt"))
    print(q1(values))
    print(q2(values))
    print([int(s.strip()) for s in re.split("->|,", values[0])])


if __name__ == "__main__":
    main()
