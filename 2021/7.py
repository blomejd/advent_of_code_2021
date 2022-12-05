import re
from utils import read_delimited
from collections import Counter
from math import floor
from statistics import median, mean


def q1(values):
    m = median(values)
    return sum(abs(v - m) for v in values)


def q2_f(values):
    minmiumm, maximum = min(values), max(values)
    m = floor(mean(values))
    print(m)
    lowest_fuel = sum(abs(v - m) * (abs(v - m) + 1) / 2 for v in values)
    for x in range(minmiumm, maximum + 1):
        current = sum(abs(v - x) * (abs(v - x) + 1) / 2 for v in values)
        if current < lowest_fuel:
            lowest_fuel = current
            print(x)

    return lowest_fuel


def q2(values):
    m = floor(mean(values))
    print(m)
    lowest_fuel = sum(abs(v - m) * (abs(v - m) + 1) / 2 for v in values)
    print(lowest_fuel)
    for x in range(m - 1000, m + 1000):
        current = 0
        for v in values:
            current += sum(n for n in range(abs(v - x) + 1))
        if current < lowest_fuel:
            lowest_fuel = current
            print(x)
            print(lowest_fuel)

    return lowest_fuel


def main():
    values = [int(c) ** 3 for c in read_delimited("7.txt", ",")[0]]
    print(values)
    print(q1(values))
    print(q2(values))


if __name__ == "__main__":
    main()
