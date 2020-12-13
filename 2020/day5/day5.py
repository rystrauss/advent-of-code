def get_seat_id(code):
    low = 0
    high = 128

    for c in code[:7]:
        if c == "F":
            high -= (high - low) // 2
        else:
            low += (high - low) // 2

    assert low == high - 1

    left = 0
    right = 8

    for c in code[-3:]:
        if c == "L":
            right -= (right - left) // 2
        else:
            left += (right - left) // 2

    assert left == right - 1

    return low * 8 + left


def main():
    with open("input.txt", "r") as fp:
        passes = [line.strip() for line in fp.readlines()]

    seat_ids = [get_seat_id(p) for p in passes]

    print("Part I:", max(seat_ids))

    seat_ids = list(sorted(seat_ids))
    your_seat = (set(range(seat_ids[0], seat_ids[-1] + 1)) - set(seat_ids)).pop()
    print("Part II:", your_seat)


if __name__ == "__main__":
    main()
