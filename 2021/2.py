from utils import read_delimited


def q1(values):
    height = 0
    distance = 0
    for command, number in values:
        number = int(number)
        if command == "forward":
            distance += number
        if command == "down":
            height += number
        if command == "up":
            height -= number
    print(height * distance)


def q2(values):
    height = distance = aim = 0
    actions = {
        "forward": lambda x: (height + aim * x, distance + x, aim),
        "down": lambda x: (height, distance, aim + x),
        "up": lambda x: (height, distance, aim - x),
    }

    for command, number in values:
        height, distance, aim = actions[command](int(number))
    print(height * distance)


def main():
    values = list(read_delimited("2.txt", " "))
    q1(values)
    q2(values)


if __name__ == "__main__":
    main()
