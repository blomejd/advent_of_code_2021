from collections import deque
from functools import reduce
from pathlib import Path
from statistics import median
from typing import Iterator

from utils import read_trimmed

OPENERS = {"(", "[", "{", "<"}
MAP = {"(": ")", "[": "]", "{": "}", "<": ">"}

SCORE_MAP = {")": 3, "]": 57, "}": 1197, ">": 25137}
SCORE_MAP_2 = {"(": 1, "[": 2, "{": 3, "<": 4}


def q1(values):
    score = 0
    for line in values:
        stack = deque()
        for c in line:
            if c in OPENERS:
                stack.append(c)
                continue
            if not stack:
                break
            expected = MAP[stack.pop()]
            if c != expected:
                score += SCORE_MAP[c]
                break
    return score


def score_line(line):
    stack = deque()
    for c in line:
        if c in OPENERS:
            stack.append(c)
            continue
        if not stack or c != MAP[stack.pop()]:
            return 0
    f = lambda score, c: score * 5 + SCORE_MAP_2[c]
    return reduce(f, reversed(stack), 0)


def q2(values):
    scores = [score_line(line) for line in values]
    scores = [s for s in scores if s]
    return median(scores)


def main():
    values = read_trimmed("./10.txt")
    print(q1(values))
    print(q2(values))


if __name__ == "__main__":
    main()
