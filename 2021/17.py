from pathlib import Path
from typing import Iterator
from utils import get_neighbors_n_dimensional, read_trimmed
from collections import deque, defaultdict, namedtuple
from statistics import median


target_x_min = 137
target_x_max = 171
target_y_min = -98
target_y_max = -73

# target_x_min = 20
# target_x_max = 30
# target_y_min = -10
# target_y_max = -5


def follow_path(x_vel, y_vel):
    x, y = 0, 0
    while (x_vel != 0 or (target_x_min <= x <= target_x_max)) and y > target_y_min:
        x += x_vel
        y += y_vel
        x_vel = x_vel if x_vel == 0 else x_vel - 1
        y_vel -= 1
        if (target_x_min <= x <= target_x_max) and (target_y_min <= y <= target_y_max):
            return True
    return False


def iter_vels():
    for x_vel in range(0, target_x_max + 1):
        for y_vel in range(target_y_min, -target_y_min):
            yield x_vel, y_vel
        print(x_vel)


def q1():
    return sum(follow_path(x, y) for x, y in iter_vels())


def main():
    print(q1())


if __name__ == "__main__":
    main()
