def main():
    elves = [[]]

    with open("input.txt", "r") as fp:
        for line in fp.readlines():
            if line == "\n":
                elves.append([])
            else:
                elves[-1].append(int(line.strip()))

    totals = list(sorted(map(sum, elves)))

    print(totals[-1])
    print(sum(totals[-3:]))


if __name__ == '__main__':
    main()
