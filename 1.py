from utils import read_trimmed
from heapq import heappush, nlargest


def q1(values):
    biggest = 0
    current = 0
    for v in values:
        if v:
            current += int(v)
        else:
            if current > biggest:
                biggest = current
            current = 0
    return biggest


def q2(values):
    current = 0
    heap = []
    for v in values:
        if v:
            current += int(v)
        else:
            heappush(heap, current)
            current = 0
    return sum(nlargest(3, heap))


def main():
    values = read_trimmed("./1.txt")
    print(q1(values))
    print(q2(values))


if __name__ == "__main__":
    main()
