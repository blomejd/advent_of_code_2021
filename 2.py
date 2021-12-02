from utils import generate_delimited


def q1(values):
    print(list(values))


def q2(values):
    pass


def main():
    values = generate_delimited("2.txt", ",")
    q1(values)
    q2(values)


if __name__ == "__main__":
    main()
