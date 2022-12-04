def range_contains(r1: range, r2: range) -> bool:
    return r1.start <= r2.start and r1.stop >= r2.stop


def ranges_overlap(r1: range, r2: range) -> bool:
    return bool(set(r1).intersection(set(r2)))


def main():
    pairs = []

    with open("input.txt", "r") as fp:
        for line in fp.readlines():
            r1, r2 = line.strip().split(",")
            l1, u1 = r1.split("-")
            l2, u2 = r2.split("-")
            pairs.append(
                (
                    range(int(l1), int(u1) + 1),
                    range(int(l2), int(u2) + 1),
                )
            )

    total = 0

    for r1, r2 in pairs:
        total += int(range_contains(r1, r2) or range_contains(r2, r1))

    print(total)

    total = 0

    for r1, r2 in pairs:
        total += int(ranges_overlap(r1, r2))

    print(total)


if __name__ == "__main__":
    main()
