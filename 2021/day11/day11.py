import itertools
from copy import copy


def get_neighbors(row, col):
    for i in range(-1, 2):
        for j in range(-1, 2):
            x = row + i
            y = col + j

            if (i == j == 0) or x < 0 or x >= 10 or y < 0 or y >= 10:
                continue

            yield x, y


def simulate(initial_energies, num_steps):
    energies = copy(initial_energies)
    num_flashes = 0

    for _ in range(num_steps):

        for k in energies.keys():
            energies[k] += 1

        should_reset = set()

        while max(energies.values()) > 9:
            for i, j in itertools.product(range(10), repeat=2):

                if energies[i, j] > 9:
                    for x, y in get_neighbors(i, j):
                        energies[x, y] += 1

                    num_flashes += 1
                    should_reset.add((i, j))

            for i, j in should_reset:
                energies[i, j] = 0

    return num_flashes


def first_synchronize(initial_energies):
    energies = copy(initial_energies)

    for step in itertools.count(1):

        for k in energies.keys():
            energies[k] += 1

        should_reset = set()
        num_flashes = 0

        while max(energies.values()) > 9:
            for i, j in itertools.product(range(10), repeat=2):

                if energies[i, j] > 9:
                    for x, y in get_neighbors(i, j):
                        energies[x, y] += 1

                    num_flashes += 1
                    should_reset.add((i, j))

            for i, j in should_reset:
                energies[i, j] = 0

        if num_flashes == 100:
            return step


def main():
    energies = dict()

    with open("input.txt", "r") as fp:
        for i, line in enumerate(fp.readlines()):
            for j, c in enumerate(line.strip()):
                energies[i, j] = int(c)

    print(simulate(energies, 100))
    print(first_synchronize(energies))


if __name__ == "__main__":
    main()
