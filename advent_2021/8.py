import re
from collections import Counter, defaultdict
from itertools import chain
from math import floor

from utils import read_delimited


def q1(values):
    count = 0
    values = [v[1] for v in values]

    for v in chain(*values):
        if len(v) in {2, 3, 4, 7}:
            count += 1
    return count


def q2(values):
    total = 0
    for v in values:
        segment_map = {}
        segments_by_length = defaultdict(list)
        for s in v[0]:
            segments_by_length[len(s)].append(set(s))

        # Only digits with these lengths
        segment_map[1] = segments_by_length[2][0]
        segment_map[4] = segments_by_length[4][0]
        segment_map[7] = segments_by_length[3][0]
        segment_map[8] = segments_by_length[7][0]

        # 3 is the only 5 segment digit that overlaps 1
        segment_map[3] = next(s for s in segments_by_length[5] if segment_map[1].issubset(s))
        # 9 is the only 6 segment digit that overlaps 4
        segment_map[9] = next(s for s in segments_by_length[6] if segment_map[4].issubset(s))
        # 6 is the only 6 segment digit that doesn't overlap 1
        segment_map[6] = next(s for s in segments_by_length[6] if not segment_map[1].issubset(s))
        segment_map[0] = next(
            s for s in segments_by_length[6] if s not in (segment_map[6], segment_map[9])
        )
        segment_map[5] = next(s for s in segments_by_length[5] if s.issubset(segment_map[6]))
        segment_map[2] = next(
            s for s in segments_by_length[5] if s not in (segment_map[5], segment_map[3])
        )
        reverse_segment_map = {"".join(sorted(v)): k for k, v in segment_map.items()}

        numbers = [reverse_segment_map["".join(sorted(s))] for s in v[1]]
        total += int("".join(str(n) for n in numbers))
    return total


def q2_temp(values):
    """
    2 segments -> 1
    3 segments -> 7
    4 segments -> 4
    5 segments -> 2, 3, 5
    6 segments -> 6, 9
    7 segments -> 8
    """
    v = values[0]
    letters = {"a", "b", "c", "d", "e", "f", "g"}
    positions = ("top", "top-left", "top-right", "middle", "bottom-left", "bottom-right", "bottom")
    segment_options = {p: {*letters} for p in positions}
    segments_by_length = defaultdict(list)
    for s in v[0]:
        segments_by_length[len(s)].append(set(s))
    segment_options["top-right"] = {s for s in segments_by_length[2][0]}
    segment_options["bottom-right"] = {s for s in segments_by_length[2][0]}
    segment_options["top"] = {s for s in segments_by_length[3][0] - segments_by_length[2][0]}

    temp = segments_by_length[6][0].symmetric_difference(segments_by_length[6][1])
    segment_options["top-right"] &= temp
    segment_options["bottom-right"] -= temp

    placed = set().union(*(s for s in segment_options.values() if len(s) == 1))
    for s in ("top-left", "middle", "bottom-left", "bottom"):
        segment_options[s] -= placed
    segment_options["top-left"] &= segments_by_length[4][0]
    segment_options["middle"] &= segments_by_length[4][0]

    temp = segments_by_length[5][0] & segments_by_length[5][1] & segments_by_length[5][2]
    for s in ("top-left", "bottom-left"):
        segment_options[s] -= temp
    placed = set().union(*(s for s in segment_options.values() if len(s) == 1))
    for s in ("middle", "bottom", "bottom-left"):
        segment_options[s] -= placed
    placed = set().union(*(s for s in segment_options.values() if len(s) == 1))

    segment_options["bottom"] -= placed

    print(segment_options)
    return []


def main():
    values = [[c.strip().split(" ") for c in s] for s in read_delimited("8.txt", "|")]
    print(q1(values))
    print(q2(values))


if __name__ == "__main__":
    main()
