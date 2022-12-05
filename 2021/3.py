from utils import read_trimmed
from collections import Counter


def invert(values):
    inversion = [[] for _ in range(len(values[0]))]
    for value in values:
        for i, bit in enumerate(value):
            inversion[i].append(bit)
    return inversion


def q1(values):
    inversion = invert(values)
    counts = [Counter(row) for row in inversion]
    gamma = [count.most_common()[0][0] for count in counts]
    epsilon = [count.most_common()[-1][0] for count in counts]
    return int("".join(gamma), 2) * int("".join(epsilon), 2)


def oxygen(values):
    if len(values[0]) == 0:
        return ""
    count = Counter(v[0] for v in values)
    if count["0"] == count["1"]:
        most_common = "1"
    else:
        most_common = count.most_common()[0][0]
    return most_common + oxygen([v[1:] for v in values if v[0] == most_common])


def co2(values):
    if len(values[0]) == 0:
        return ""
    count = Counter(v[0] for v in values)
    if count["0"] == count["1"]:
        least_common = "0"
    else:
        least_common = count.most_common()[-1][0]
    return least_common + co2([v[1:] for v in values if v[0] == least_common])


def q2(values):
    return int("".join(oxygen(values)), 2) * int("".join(co2(values)), 2)


def main():
    values = list(read_trimmed("3.txt"))
    print(q1(values))
    print(q2(values))


if __name__ == "__main__":
    main()
