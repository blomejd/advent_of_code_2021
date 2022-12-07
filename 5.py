import re
from collections import deque
from itertools import zip_longest

from utils import grouper, read_lines

f = "./" + __file__.replace("py", "txt")


def parse(f):
    lines = read_lines(f)
    stack_rows = lines[:8]
    stacks = []
    for row in stack_rows[::-1]:
        row = row.replace("\n", "")
        for stack, chunk in zip_longest(stacks, grouper(iter(row), 4, fillvalue="")):
            v = re.sub(r"[\[\] ]", "", "".join(chunk))
            if stack is None:
                stack = deque()
                stacks.append(stack)
            if v:
                stack.append(v)

    command_rows = lines[10:]
    command_g = (re.split(" ", row.strip()) for row in command_rows)
    commands = [(int(c[1]), int(c[3]) - 1, int(c[5]) - 1) for c in command_g]
    return stacks, commands


def q1(values):
    stacks, commands = values
    for count, i_from, i_to in commands:
        s_from, s_to = stacks[i_from], stacks[i_to]
        s_to.extend(s_from.pop() for _ in range(count))
    return "".join(s[-1] for s in stacks)


def q2(values):
    stacks, commands = values
    for count, i_from, i_to in commands:
        s_from, s_to = stacks[i_from], stacks[i_to]
        s = deque(s_from.pop() for _ in range(count))
        s.reverse()
        s_to.extend(s)
    return "".join(s[-1] for s in stacks)


def main():
    # print(parse(f))
    print(q1(parse(f)))
    print(q2(parse(f)))


if __name__ == "__main__":
    main()
