def main():
    with open("input.txt", "r") as fp:
        instructions = fp.readlines()

    def parse(s):
        direction, amount = s.strip().split()
        return direction, int(amount)

    instructions = list(map(parse, instructions))

    x, y = 0, 0

    for direction, amount in instructions:
        if direction == "forward":
            x += amount
        elif direction == "up":
            y -= amount
        else:
            y += amount

    print(x * y)

    x, y, z = 0, 0, 0

    for direction, amount in instructions:
        if direction == "forward":
            x += amount
            y += z * amount
        elif direction == "up":
            z -= amount
        else:
            z += amount

    print(x * y)


if __name__ == '__main__':
    main()
