from collections import deque
from statistics import median

PAIRS = {"[": "]", "(": ")", "{": "}", "<": ">"}


def check_line(s):
    stack = deque()

    first_mismatch = None

    for c in s:
        if c in PAIRS:
            stack.append(c)
        else:
            if c != PAIRS[stack.pop()]:
                first_mismatch = first_mismatch or c

    if first_mismatch is not None:
        return first_mismatch

    return stack


def main():
    with open("input.txt", "r") as fp:
        lines = [l.strip() for l in fp.readlines()]

    values = {")": 3, "]": 57, "}": 1197, ">": 25137}
    s = 0

    for l in lines:
        r = check_line(l)
        if not isinstance(r, str):
            continue

        s += values[r]

    print(s)

    values = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []

    for l in lines:
        r = check_line(l)
        if isinstance(r, str):
            continue

        s = 0

        while r:
            s = s * 5 + values[PAIRS[r.pop()]]

        scores.append(s)

    print(median(scores))


if __name__ == "__main__":
    main()
