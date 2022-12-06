from utils import read_trimmed


def fake_ord(c):
    if c == c.lower():
        return ord(c) - 96
    return ord(c) - 64 + 26


def halve(s):
    return set(s[: len(s) // 2]) & set(s[len(s) // 2 :])


def q1(values):
    return sum(sum(fake_ord(c) for c in halve(v)) for v in values)


def grouper(values):
    g = iter(values)
    while True:
        try:
            yield (next(g), next(g), next(g))
        except StopIteration:
            return


def q2(values):
    sets = [set(a) & set(b) & set(c) for (a, b, c) in grouper(values)]
    return sum(fake_ord(c) for s in sets for c in s)


def main():
    s = "abcdefghijklmnopqrstuvwxyz"
    print([fake_ord(c) for c in s])
    print([fake_ord(c) for c in s.upper()])
    values = read_trimmed("./3.txt")
    print(q1(values))
    print(q2(values))


if __name__ == "__main__":
    main()
