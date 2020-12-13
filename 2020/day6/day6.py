def main():
    with open("input.txt", "r") as fp:
        groups = fp.read().strip().split("\n\n")

    total = 0
    for group in groups:
        total += len(set(group.replace("\n", "")))

    print("Part I:", total)

    total = 0
    for group in groups:
        people = [set(s) for s in group.split("\n")]
        total += len(set.intersection(*people))

    print("Part II:", total)


if __name__ == "__main__":
    main()
