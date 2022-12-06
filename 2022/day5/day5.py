from collections import deque
from copy import deepcopy
from typing import NamedTuple


class Move(NamedTuple):
    amount: int
    start: int
    end: int


def main():
    with open("input.txt", "r") as fp:
        crates_str, moves_str = fp.read().rstrip().split("\n\n")

    crates_lines = crates_str.split("\n")
    num_stacks = int(crates_lines[-1].split()[-1])

    stacks = [deque([]) for _ in range(num_stacks)]

    for line in reversed(crates_lines[:-1]):
        for i in range(0, len(line), 4):
            col = line[i : i + 3]
            if not col.isspace():
                stacks[i // 4].append(col[1])

    moves = []

    for line in moves_str.split("\n"):
        parts = line.split(" ")
        moves.append(
            Move(
                amount=int(parts[1]),
                start=int(parts[3]),
                end=int(parts[5]),
            )
        )

    part1_stacks = deepcopy(stacks)

    for move in moves:
        for _ in range(move.amount):
            part1_stacks[move.end - 1].append(part1_stacks[move.start - 1].pop())

    answer = "".join(map(lambda d: d[-1], part1_stacks))
    print(answer)

    part2_stacks = deepcopy(stacks)

    for move in moves:
        crane = deque([])
        for _ in range(move.amount):
            crane.append(part2_stacks[move.start - 1].pop())
        crane.reverse()
        part2_stacks[move.end - 1].extend(crane)

    answer = "".join(map(lambda d: d[-1], part2_stacks))
    print(answer)


if __name__ == "__main__":
    main()
