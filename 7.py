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
    sub_dirs: dict[str, Dir]
    files: list[File]
    name: str = ""
    parent: Dir | None = None

    def __init__(self, name: str, parent: Dir | None = None) -> None:
        self.name = name
        self.parent = parent
        self.files = []
        self.sub_dirs = {}

    @property
    def size(self) -> int:
        immediate = sum(child.size for child in self.files)
        if not self.sub_dirs:
            return immediate
        nested = sum(child.size for child in self.sub_dirs.values())
        return immediate + nested

    def big_dirs(self, target) -> list[int]:
        if self.size < target:
            return []
        children = [child.big_dirs(target) for child in self.sub_dirs.values()]
        return [self.size, *chain(*children)]

    def lil_dirs(self) -> list[int]:
        dirs = [*chain.from_iterable(child.lil_dirs() for child in self.sub_dirs.values())]
        if self.size <= 100000:
            dirs.append(self.size)
        return [x for x in dirs if x <= 100000]

    def __repr__(self) -> str:
        files = "\n".join(str(child) for child in self.files)
        subdirs = "\n".join(str(child) for child in self.sub_dirs.values())
        return f"{self.name}\n{files}{subdirs}"


def parse(f) -> list[str]:
    return read_trimmed(f)


def handle_ls(values: list[str], current: Dir, i: int):
    i += 1
    while i < len(values):
        line = values[i].split(" ")
        if line[0] == "$":
            return i
        if line[0] == "dir":
            current.sub_dirs[line[1]] = Dir(name=line[1], parent=current)
        else:
            current.files.append(File(name=line[1], size=int(line[0])))
        i += 1
    return i


def build_root(values):
    root = Dir(name="/", parent=None)
    current = root
    i = 1
    while i < len(values):
        line = values[i].split(" ")
        if line[1] == "ls":
            i = handle_ls(values, current, i)
        elif line[1] == "cd":
            if line[2] == "..":
                current = current.parent
            else:
                current = current.sub_dirs[line[2]]
            i += 1
    return root


def q1(values):
    root = build_root(values)
    return sum(root.lil_dirs())


def q2(values):
    root = build_root(values)
    total = 70_000_000
    need = 30_000_000 - (total - root.size)
    return min(root.big_dirs(need))


def main():
    print(q1(parse(f)))
    print(q2(parse(f)))


if __name__ == "__main__":
    main()
