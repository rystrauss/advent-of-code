from collections import Counter


def main():
    with open("input.txt", "r") as fp:
        lines = [line.strip() for line in fp.readlines()]

    num_valid_part_1 = 0
    num_valid_part_2 = 0

    for line in lines:
        front, back = line.split(":")

        password = back.strip()

        bounds, letter = front.split(" ")
        low, high = bounds.split("-")
        low = int(low)
        high = int(high)

        counter = Counter(password)

        if low <= counter[letter] <= high:
            num_valid_part_1 += 1

        j = int(password[low - 1] == letter) + int(password[high - 1] == letter)
        num_valid_part_2 += int(j == 1)

    print("Part I:", num_valid_part_1)
    print("Part II:", num_valid_part_2)


if __name__ == "__main__":
    main()
