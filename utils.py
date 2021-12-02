from pathlib import Path
from typing import List


def read_lines(filename: str) -> List[str]:
    with Path(filename).open("r", encoding="utf-8") as f:
        return [l for l in f]


def read_trimmed(filename: str) -> List[str]:
    return [l.strip() for l in read_lines(filename)]


def read_ints(filename: str) -> List[int]:
    return [int(l) for l in read_trimmed(filename)]


def read_delimited(filename: str, delimiter: str) -> List[str]:
    return [l.split(delimiter) for l in read_trimmed(filename)]
