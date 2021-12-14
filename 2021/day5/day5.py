from collections import defaultdict


def main():
    def parse_line(s):
        start, end = s.strip().split(" -> ")
        start = tuple(map(int, start.split(",")))
        end = tuple(map(int, end.split(",")))
        return start, end

    with open("input.txt", "r") as fp:
        lines = list(map(parse_line, fp.readlines()))

    counts = defaultdict(int)

    for (x1, y1), (x2, y2) in lines:
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                counts[x1, i] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                counts[i, y1] += 1

    k = len(list(filter(lambda c: c >= 2, counts.values())))
    print(k)

    counts = defaultdict(int)

    for (x1, y1), (x2, y2) in lines:
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                counts[x1, i] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                counts[i, y1] += 1
        else:
            x_sign = 1 if x2 >= x1 else -1
            y_sign = 1 if y2 >= y1 else -1

            for i, j in zip(
                range(x1, x2 + x_sign, x_sign), range(y1, y2 + y_sign, y_sign)
            ):
                counts[i, j] += 1

    k = len(list(filter(lambda c: c >= 2, counts.values())))
    print(k)


if __name__ == "__main__":
    main()
