NUMBERS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def find_first_number(s):
    while True:
        if 48 <= ord(s[0]) <= 57:
            return s[0]

        for k, v in NUMBERS.items():
            if s.startswith(k):
                return str(v)

        s = s[1:]


def find_last_number(s):
    s = s[::-1]

    while True:
        if 48 <= ord(s[0]) <= 57:
            return s[0]

        for k, v in NUMBERS.items():
            if s.startswith(k[::-1]):
                return str(v)

        s = s[1:]


def main():
    with open("input.txt", "r") as fp:
        lines = fp.readlines()

    digits = [[c for c in line.strip() if 48 <= ord(c) <= 57] for line in lines]
    numbers = [int(x[0] + x[-1]) for x in digits]

    print("Part 1:", sum(numbers))

    numbers = [int(find_first_number(x.strip()) + find_last_number(x.strip())) for x in lines]
    print("Part 2:", sum(numbers))


if __name__ == "__main__":
    main()
