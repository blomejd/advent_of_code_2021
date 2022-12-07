from collections import Counter

from utils import read_trimmed

f = "./" + __file__.replace("py", "txt")


def parse(f):
    return read_trimmed(f)[0]


def q1(values):
    count = Counter(values[:4])
    for i, c in enumerate(values[4:]):
        if count.most_common(1)[0][1] <= 1:
            return i + 4
        count[c] += 1
        count[values[i]] -= 1
    return -1


def q2(values):
    n = 14
    count = Counter(values[:n])
    for i, c in enumerate(values[n:]):
        if count.most_common(1)[0][1] <= 1:
            return i + n
        count[c] += 1
        count[values[i]] -= 1
    return -1


def main():
    print(q1(parse(f)))
    print(q2(parse(f)))


if __name__ == "__main__":
    main()
