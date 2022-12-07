import re

from utils import read_trimmed

f = "./" + __file__.replace("py", "txt")


def parse(f):
    return [(int(d) for d in re.split(r",|-", s)) for s in read_trimmed(f)]


def contained(a, b, c, d):
    a, b, c, d = min(a, b), max(a, b), min(c, d), max(c, d)
    if a > c:
        a, b, c, d = c, d, a, b
    return b >= d


def q1(values):
    return sum(1 for (a, b, c, d) in values if (a <= c and b >= d) or (c <= a and d >= b))


def overlap(a, b, c, d):
    a, b, c, d = min(a, b), max(a, b), min(c, d), max(c, d)
    if a > c:
        a, b, c, d = c, d, a, b
    return c <= b


def q2(values):
    return sum(overlap(*v) for v in values)


def main():
    print(q1(parse(f)))
    print(q2(parse(f)))


if __name__ == "__main__":
    main()
