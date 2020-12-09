from math import prod


def check_slope(grid, run, rise):
    pos = [0, 0]
    num_trees = 0

    while pos[0] < len(grid):
        num_trees += int(grid[pos[0]][pos[1]] == '#')
        pos[0] += rise
        pos[1] = (pos[1] + run) % len(grid[0])

    return num_trees


def main():
    with open('input.txt', 'r') as fp:
        grid = [line.strip() for line in fp]

    print('Part I:', check_slope(grid, 3, 1))

    results = [
        check_slope(grid, 1, 1),
        check_slope(grid, 3, 1),
        check_slope(grid, 5, 1),
        check_slope(grid, 7, 1),
        check_slope(grid, 1, 2),
    ]
    print('Part II:', prod(results))


if __name__ == '__main__':
    main()
