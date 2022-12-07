from utils import read_trimmed

shape_score = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

wins = {
    "A": {"C", "Z"},
    "B": {"A", "X"},
    "C": {"B", "Y"},
    "X": {"C", "Z"},
    "Y": {"A", "X"},
    "Z": {"B", "Y"},
}


def score(them, us):
    if them in wins[us]:
        return 6 + shape_score[us]
    if us in wins[them]:
        return 0 + shape_score[us]
    return 3 + shape_score[us]


def q1(values):
    return sum(score(*line.split(" ")) for line in values)


def score_2(them, result):
    if result == "Y":
        return shape_score[them] + 3
    if result == "X":
        return shape_score[list(wins[them])[0]]
    us = next(k for k in wins if them in wins[k])
    return 6 + shape_score[us]


def q2(values):
    return sum(score_2(*line.split(" ")) for line in values)


def main():
    values = read_trimmed("./2.txt")
    print(q1(values))
    print(q2(values))


if __name__ == "__main__":
    main()
