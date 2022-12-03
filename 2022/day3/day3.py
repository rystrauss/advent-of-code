from functools import reduce


def main():
    rucks = []

    with open("input.txt", "r") as fp:
        for line in fp:
            rucks.append(line.strip())

    total_priority = 0

    for r in rucks:
        n = len(r)
        c1 = set(r[: n // 2])
        c2 = set(r[n // 2 :])

        common_item = c1.intersection(c2).pop()

        total_priority += (
            (ord(common_item.lower()) - ord("a")) + 26 * (common_item.isupper()) + 1
        )

    print(total_priority)

    total_priority = 0

    for i in range(0, len(rucks), 3):
        e1 = set(rucks[i])
        e2 = set(rucks[i + 1])
        e3 = set(rucks[i + 2])

        badge = reduce(set.intersection, (e1, e2, e3)).pop()

        total_priority += (
            (ord(badge.lower()) - ord("a")) + 26 * (badge.isupper()) + 1
        )

    print(total_priority)


if __name__ == "__main__":
    main()
