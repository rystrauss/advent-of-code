import itertools
from math import prod


def main():
    with open('input.txt', 'r') as fp:
        nums = [int(line) for line in fp.readlines()]

    # Part I
    for subset in itertools.combinations(nums, 2):
        if sum(subset) == 2020:
            print(prod(subset))

    # Part II
    for subset in itertools.combinations(nums, 3):
        if sum(subset) == 2020:
            print(prod((subset)))


if __name__ == '__main__':
    main()
