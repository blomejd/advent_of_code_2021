from __future__ import annotations

from itertools import chain

from utils import read_trimmed

f = __file__.replace("py", "txt")


class File:
    name: str = ""
    size: int = 0

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def __repr__(self) -> str:
        return f"{self.name} {self.size}"


class Dir:
    name: str = ""
    sub_dirs: dict[str, Dir] = {}
    files: list[File] = []
    parent: Dir | None = None

    def __init__(self, name: str, parent: Dir | None = None) -> None:
        self.name = name
        self.parent = parent

    @property
    def size(self) -> int:
        immediate = sum(child.size for child in self.files)
        nested = sum(child.size for child in self.sub_dirs.values())
        return immediate + nested

    def big_dirs(self) -> list[tuple[str, int]]:
        if self.size < 100000:
            return []
        children = [child.big_dirs() for child in self.sub_dirs.values()]
        return [(self.name, self.size), *chain(*children)]

    def __repr__(self) -> str:
        files = "\n".join(str(child) for child in self.files)
        # subdirs = "\n".join(str(child) for child in self.sub_dirs.values())
        # return f"{self.name}\n{files}{subdirs}"
        return f"{self.name}\n{files}"


def parse(f) -> list[str]:
    return read_trimmed(f)


def handle_ls(values: list[str], current: Dir, i: int):
    i += 1
    while i < len(values):
        line = values[i].split(" ")
        print("ding", line)
        if line[0] == "$":
            return i
        if line[0] == "dir":
            current.sub_dirs[line[1]] = Dir(line[1], current)
        else:
            current.files.append(File(name=line[1], size=int(line[0])))
        i += 1
    return i


def q1(values):
    root = Dir("/")
    current = root
    i = 1
    while i < len(values):
        line = values[i].split(" ")
        print("dong", line)
        print(current)
        if line[1] == "ls":
            i = handle_ls(values, current, i)
        elif line[1] == "cd":
            if line[2] == "..":
                current = current.parent
            else:
                current = current.sub_dirs[line[2]]
            i += 1

    return root.big_dirs()


def q2(values):
    return 0


def main():
    print(q1(parse(f)))
    # print(q2(parse(f)))


if __name__ == "__main__":
    main()
