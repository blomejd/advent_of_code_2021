from collections import defaultdict, deque, namedtuple
from pathlib import Path
from statistics import median
from typing import Iterator

from utils import get_neighbors_n_dimensional, read_trimmed


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def reduce(self):
        while self.explode() or self.split():
            # print(self)
            pass

    def explode(self):
        left_neighbor = None
        g = self.traverse_left()
        while True:
            try:
                node, depth = next(g)
            except StopIteration:
                return False
            if depth >= 4 and not node.is_leaf() and node.left.is_leaf() and node.right.is_leaf():
                # print("explode")
                # print(self)
                if left_neighbor:
                    left_neighbor.value += node.left.value
                try:
                    next(g)
                    next(g)
                    right_neighbor, depth = next(g)
                    while not right_neighbor.is_leaf():
                        right_neighbor, depth = next(g)
                    right_neighbor.value += node.right.value
                except StopIteration:
                    node.reset()
                    return True
                node.reset()
                return True

            if node.is_leaf():
                left_neighbor = node

    def split(self):
        g = self.traverse_left()
        while True:
            try:
                node, depth = next(g)
            except StopIteration:
                return False
            if node.is_leaf() and node.value >= 10:
                # print("split")
                # print(self)
                node.left = Node((node.value) // 2)
                node.right = Node((node.value + 1) // 2)
                node.value = None
                return True

    def get_right(self):
        if isinstance(self.right, int):
            return self.right
        return self.right.get_right()

    def get_left(self):
        if isinstance(self.left, int):
            return self
        return self.left.get_left()

    def next_right(self):
        if self.parent == None:
            return None
        if self == self.parent.right:
            return self.parent.next_right()
        return self.parent.right.get_left()

    def traverse_left(self, depth=0):
        if self.is_leaf():
            yield self, depth
        else:
            yield self, depth
            yield from self.left.traverse_left(depth + 1)
            yield from self.right.traverse_left(depth + 1)

    @staticmethod
    def add(left_node, right_node):
        n = Node(None, left_node, right_node)
        left_node.parent = n
        right_node.parent = n
        return n

    def is_leaf(self):
        return self.left == None and self.right == None

    def reset(self):
        self.left = None
        self.right = None
        self.value = 0

    def magnitude(self):
        if self.is_leaf():
            return self.value
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def __repr__(self):
        if self.value is not None:
            return str(self.value)
        return f"({self.left}, {self.right})"

    def copy(self):
        if self.is_leaf():
            return Node(self.value)
        return Node(None, self.left.copy(), self.right.copy())


def q1(values):
    root = values[0]
    for node in values[1:]:
        root = Node.add(root, node)
        root.reduce()

    return root.magnitude()


def q2(values):
    max = 0
    for i, a in enumerate(values):
        for j, b in enumerate(values):
            if i == j:
                continue
            n = Node.add(a.copy(), b.copy())
            n.reduce()
            mag = n.magnitude()
            if mag > max:
                print(i, j)
                max = mag
    return max


def create_branch(line):
    if line.isnumeric():
        return Node(int(line))
    comma_index = find_comma(line)
    left_str = line[1:comma_index]
    left = create_branch(left_str)
    right_str = line[comma_index + 1 : -1]
    right = create_branch(right_str)
    parent = Node(None, left, right)
    left.parent = parent
    right.parent = parent
    return parent


def find_comma(str):
    count = 0
    for i, c in enumerate(str[1:]):
        if c == "[":
            count += 1
        if c == "]":
            count -= 1
        if count == 0 and c == ",":
            return i + 1


def parse_values(filename):
    return [create_branch(line) for line in read_trimmed(filename)]
    # values = [s.split(",") for s in read_trimmed(filename)]
    # return [(int(left[1:]), int(right[:-1])) for left, right in values]


def main():
    filename = "./18.txt"
    values = [*parse_values(filename)]
    print(values[0])
    print(values[8])
    print(q1([values[8], values[0]]))

    values = [*parse_values(filename)]
    print(q2(values))


if __name__ == "__main__":
    main()
