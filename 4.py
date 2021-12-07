from utils import read_trimmed


class Board:
    height = 0
    width = 0

    def __init__(self, raw_board):
        self.rows = [[int(c.strip()) for c in row.split(" ") if c] for row in raw_board]
        self.height = len(self.rows)
        self.width = len(self.rows[0])
        self.marks = [[False] * self.width for _ in range(self.height)]

    def iter_indices(self):
        return ((i, j) for i in range(self.width) for j in range(self.height))

    def iter_values(self):
        return ((i, j, self.rows[i][j]) for i, j in self.iter_indices())

    def iter_marks(self):
        return ((i, j, self.marks[i][j]) for i, j in self.iter_indices())

    def mark(self, c):
        for i, j, value in self.iter_values():
            if value == c:
                self.marks[i][j] = True

    def check(self):
        if any(all(mark_row) for mark_row in self.marks):
            return True
        return any(all(r[i] for r in self.marks) for i in range(self.width))

    def score(self, number):
        total = sum(v for i, j, v in self.iter_values() if not self.marks[i][j])
        return total * number


def mark_check_test(raw_board):
    """ Test mark and check for board 0 """
    b = Board(raw_board)
    b.mark(97)
    assert not b.check()
    b.mark(81)
    assert not b.check()
    b.mark(12)
    assert not b.check()
    b.mark(80)
    assert not b.check()
    b.mark(52)
    assert b.check()

    b = Board(raw_board)
    b.mark(27)
    assert not b.check()
    b.mark(80)
    assert not b.check()
    b.mark(23)
    assert not b.check()
    b.mark(43)
    assert not b.check()
    b.mark(78)
    assert b.check()


def parse_inputs(values):
    numbers = [int(c) for c in values[0].split(",")]

    raw_boards = values[2:]
    boards = [Board(raw_boards[i : i + 5]) for i in range(0, len(raw_boards), 6)]
    return numbers, boards


def q1(values):
    numbers, boards = parse_inputs(values)

    for number in numbers:
        for board in boards:
            board.mark(number)
            if board.check():
                return board.score(number)
    assert False


def q2(values):
    numbers, boards = parse_inputs(values)

    for number in numbers:
        for board in boards[:]:
            board.mark(number)
            if board.check():
                if len(boards) == 1:
                    return board.score(number)
                boards.remove(board)
    assert False


def main():
    values = list(read_trimmed("4.txt"))
    print(q1(values))
    print(q2(values))


if __name__ == "__main__":
    main()
