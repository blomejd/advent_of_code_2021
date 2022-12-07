from collections import defaultdict, deque
from pathlib import Path
from statistics import median
from typing import Iterator

from utils import get_neighbors_n_dimensional, read_trimmed


class Node:
    def __init__(self, value):
        self.value = value
        self.connections = {}
        if value in {"end", "start"}:
            self.max_visits = 1
        elif value == value.lower():
            self.max_visits = 2
        else:
            self.max_visits = None

    def link(self, node):
        self.connections[node.value] = node

    def __repr__(self):
        return f"{self.value}: {self.connections.keys()}"

    def find_paths(self, visited, small_flag=False):
        if self.value == "end":
            return [[]]

        paths = []
        for connection in self.connections.values():
            c_v = connection.value
            if c_v == "start":
                continue
            c_visited = visited.copy()
            c_small_flag = small_flag
            if c_v == c_v.lower():
                if c_v in visited:
                    if small_flag:
                        continue
                    else:
                        c_small_flag = True
                c_visited.add(c_v)

            for path in connection.find_paths(c_visited, c_small_flag):
                paths.append([self.value] + path)
        return paths


def q1(values):
    nodes = {}
    for value in values:
        if value[0] not in nodes:
            nodes[value[0]] = Node(value[0])
        if value[1] not in nodes:
            nodes[value[1]] = Node(value[1])
        nodes[value[0]].link(nodes[value[1]])
        nodes[value[1]].link(nodes[value[0]])

    node = nodes["start"]
    paths = list(node.find_paths({"start"}))
    return len(paths)


def q2(grid):
    return 0


def main():
    filename = "./12.txt"
    values = [s.split("-") for s in read_trimmed(filename)]
    print(q1(values))
    values = read_trimmed(filename)
    print(q2(values))


if __name__ == "__main__":
    main()
