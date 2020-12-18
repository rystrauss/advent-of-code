import itertools
import operator
from collections import Counter


def elementwise_sum(a, b):
    return tuple(map(operator.add, a, b))


def neighbors(query, dim=3):
    deltas = itertools.product([-1, 0, 1], repeat=dim)
    for d in deltas:
        if d != (0,) * dim:
            yield elementwise_sum(query, d)


def do_iteration(active_cells, dim=3):
    counter = Counter(n for c in active_cells for n in neighbors(c, dim=dim))
    next_active_cells = {
        c for c in counter if counter[c] == 3 or (counter[c] == 2 and c in active_cells)
    }
    return next_active_cells


def main():
    initial_active_cells = set()

    with open("input.txt", "r") as fp:
        for x, line in enumerate(fp):
            for y, c in enumerate(line.strip()):
                if c == "#":
                    initial_active_cells.add((x, y, 0))

    active_cells = initial_active_cells
    for _ in range(6):
        active_cells = do_iteration(active_cells, dim=3)

    print("Part I:", len(active_cells))

    active_cells = set(map(lambda x: (*x, 0), initial_active_cells))
    for _ in range(6):
        active_cells = do_iteration(active_cells, dim=4)

    print("Part II:", len(active_cells))


if __name__ == "__main__":
    main()
