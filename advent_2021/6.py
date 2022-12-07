import re
from collections import Counter

from utils import read_delimited

reset_val = 8


def q1(values):
    values = values[:]
    for _ in range(80):
        for i, v in enumerate(values[:]):
            if v == 0:
                values[i] = 6
                values.append(8)
            else:
                values[i] -= 1
    return len(values)


def q2(values):
    count = Counter(values)
    for _ in range(256):
        count = {(i - 1): count[i] for i in range(9)}
        count[6] += count[-1]
        count[8] = count.pop(-1)
    return sum(count.values())


def main():
    values = [int(c) for c in read_delimited("6.txt", ",")[0]]
    print(q1(values))
    print(q2(values))


if __name__ == "__main__":
    main()
