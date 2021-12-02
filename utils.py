from pathlib import Path
from typing import Iterator, List


def generate_lines(filename: str) -> List[str]:
    with Path(filename).open("r", encoding="utf-8") as f:
        return [l for l in f]


def generate_trimmed(filename: str) -> Iterator[str]:
    return (l.strip() for l in generate_lines(filename))


def generate_ints(filename: str) -> Iterator[int]:
    return (int(l) for l in generate_trimmed(filename))


def generate_delimited(filename: str, delimiter: str) -> Iterator[str]:
    return (l.split(delimiter) for l in generate_trimmed(filename))
