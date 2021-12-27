from copy import deepcopy

import matplotlib.pyplot as plt

def fold(grid, direction, location):
    new_grid = deepcopy(grid)

    for x, y in grid:
        if direction == "x" and x >= location:
            new_grid.remove((x, y))
            new_grid.add((location - (x - location), y))
        elif direction == "y" and y >= location:
            new_grid.remove((x, y))
            new_grid.add((x, location - (y - location)))

    return new_grid


def main():
    with open("input.txt", "r") as fp:
        coordinates, folds = fp.read().split("\n\n")

    grid = set(
        map(lambda s: tuple(map(int, s.strip().split(","))), coordinates.split("\n"))
    )

    def parse_fold(s):
        a, b = s[11:].split("=")
        return a, int(b)

    folds = list(map(parse_fold, folds.strip().split("\n")))

    print(len(fold(grid, *folds[0])))

    folded_grid = grid
    for f in folds:
        folded_grid = fold(folded_grid, *f)

    xs = [t[0] for t in folded_grid]
    ys = [-t[1] for t in folded_grid]

    plt.scatter(xs, ys)
    plt.gca().set_aspect("equal")
    plt.show()


if __name__ == "__main__":
    main()
