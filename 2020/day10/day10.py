from collections import Counter, defaultdict


def main():
    with open("input.txt", "r") as fp:
        adapters = [int(line) for line in fp]

    adapters = list(sorted(adapters))
    deltas = [adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1)]
    counter = Counter(deltas)

    print("Part I:", (counter[1] + 1) * (counter[3] + 1))

    paths = defaultdict(int)
    paths[0] = 1

    for a in adapters + [max(adapters) + 3]:
        paths[a] = paths[a - 1] + paths[a - 2] + paths[a - 3]

    print("Part II:", paths[max(adapters) + 3])


if __name__ == "__main__":
    main()
