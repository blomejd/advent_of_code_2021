from collections import Counter, defaultdict, deque, namedtuple
from pathlib import Path
from statistics import median
from typing import Iterator

from utils import get_neighbors_n_dimensional, read_trimmed


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __repr__(self):
        if self.next is None:
            return self.value
        return f"{self.value}{self.next}"


class MemoziedParser:
    def __init__(self, base):
        self.base = base
        self.m = {}
        self.chunk_size = 10000

    def generate_chunks(self, string):
        for start in range(0, len(string), self.chunk_size):
            end = start + self.chunk_size
            yield string[start:end], string[end - 1 : end + 1]

    def countdown_parse(self, string, count):
        if count == 0:
            return Counter(string)
        r = Counter()
        for chunk, extra in self.generate_chunks(string):
            r += self.countdown_parse(self.insert_chars(chunk), count - 1)
            bonus = Counter(self.base.get(extra, ""))
            # print(string, chunk, extra, bonus)
            r += bonus
        return r

    def insert_chars(self, string):
        if string in self.m:
            return self.m[string]
        s = ""
        for i, n in enumerate(string):
            s += n
            s += self.base.get(string[i : i + 2], "")
        self.m[string] = s
        return s

    def parse(self, s):
        if len(s) <= 1:
            return s
        if s in self.m:
            return self.m[s]

        for i in range(0, len(s), 10):
            chunk = s[i : i + 10]
            if chunk not in self.m:
                self.m[chunk] = self.parse(chunk)
            self.m[chunk]
        mid = len(s) // 2
        extra = self.base.get(s[mid - 1 : mid + 1], "")
        result = self.parse(s[:mid]) + extra + self.parse(s[mid:])
        self.m[s] = result
        return self.m[s]


def iter_node(node):
    current = node
    while current:
        yield current.value
        current = current.next


def q1(start, pairs):
    m = {p[0]: p[1] for p in pairs}
    parser = MemoziedParser(m)
    for _ in range(10):
        start = parser.insert_chars(start)
        # s = ""
        # for i, n in enumerate(start):
        #     s += n
        #     if start[i : i + 2] in m:
        #         s += m[start[i : i + 2]]
        # start = s
    c = Counter(start)
    return c.most_common(1)[0][1] - c.most_common()[-1][1]


def insert_chars(string, m):
    s = ""
    for i, n in enumerate(string):
        s += n
        if string[i : i + 2] in m:
            s += m[string[i : i + 2]]
    return s


def q2(start, pairs):
    last = start[-1]
    m = {p[0]: p[1] for p in pairs}
    result = Counter([start[i : i + 2] for i in range(0, len(start) - 1)])
    for step in range(40):
        next_result = Counter()
        for s, count in result.items():
            next_result[s[0] + m[s]] += count
            next_result[m[s] + s[1]] += count
        result = next_result
    c = Counter()
    for k, v in result.items():
        c[k[0]] += v
    c[last] += 1
    print(c)
    return c.most_common(1)[0][1] - c.most_common()[-1][1]


def q2_5(start, pairs):
    m = {p[0]: p[1] for p in pairs}

    parser = MemoziedParser(m)
    parser.m = {p[0]: p[0][0] + p[1] + p[0][1] for p in pairs}

    print([*parser.generate_chunks(start)])

    c = parser.countdown_parse(start, 10)
    return c.most_common(1)[0][1] - c.most_common()[-1][1]


def generate_chunks(string, m):
    start = 0
    for i in range(len(string)):
        if string[i : i + 2] not in m:
            yield string[start : i + 1]
            start = i + 1


def q2_helper(string, m, count):
    if count == 0:
        return Counter(string)

    r = Counter()
    for chunk in generate_chunks(string, m):
        r += q2_helper(insert_chars(chunk, m), m, count - 1)

    return r


def q2_4(start, pairs):
    m = {p[0]: p[1] for p in pairs}
    c = q2_helper(start, m, 40)
    return c.most_common(1)[0][1] - c.most_common()[-1][1]


def parse_values(filename: str):
    lines = read_trimmed(filename)
    start = lines[0]
    split_lines = [s.split("->") for s in lines[2:] if s]
    pairs = [(s[0].strip(), s[1].strip()) for s in split_lines]
    return start, pairs


def main():
    filename = "./14.txt"
    start, pairs = parse_values(filename)
    print(q1(start, pairs))

    start, pairs = parse_values(filename)
    print(q2(start, pairs))


if __name__ == "__main__":
    main()


def q2_1(start, pairs):
    head = Node(start[0], None)
    current = head
    for c in start[1:]:
        current.next = Node(c, None)
        current = current.next
    print("".join([c for c in iter_node(head)]))


def q2_2(start, pairs):
    m = {p[0]: p[1] for p in pairs}
    head = Node(start[0], None)
    for step in range(40):
        current = head
        print(step)
        while current.next:
            c = current.value + current.next.value
            if c in m:
                new = Node(m[c], current.next)
                current.next = new
                current = new.next
            else:
                current = current.next

    to_add = deque()
    for step in range(40):
        # start = "".join(["".join([c, m.get(start[i : i + 2], "")]) for i, c in enumerate(start)])
        for i, n in enumerate(zip(start, to_add)):
            to_add.append(m.get(start[i : i + 2], ""))
        print(step)
    c = Counter(iter_node(head))


def q2_3(start, pairs):
    m = {p[0]: p[1] for p in pairs}

    parser = MemoziedParser(m)
    parser.m = {p[0]: p[0][0] + p[1] + p[0][1] for p in pairs}
    for step in range(40):
        print(step)
        start = parser.parse(start)
    c = Counter(start)
    return c.most_common(1)[0][1] - c.most_common()[-1][1]
