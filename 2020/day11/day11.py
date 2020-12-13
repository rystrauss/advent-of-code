from collections import defaultdict


def num_occupied_adjacent_seats(grid, r, c):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                count += int(grid[r + i, c + j] == "#")

    return count


def iterate(grid):
    new_grid = defaultdict(str)
    did_change = False

    for (r, c), state in list(grid.items()):
        if state == "L" and num_occupied_adjacent_seats(grid, r, c) == 0:
            new_grid[r, c] = "#"
            did_change = True
        elif state == "#" and num_occupied_adjacent_seats(grid, r, c) >= 4:
            new_grid[r, c] = "L"
            did_change = True
        else:
            new_grid[r, c] = grid[r, c]

    return new_grid, did_change


def num_occupied_adjacent_seats_v2(grid, r, c):
    count = 0

    # UP
    i = r - 1
    while grid[i, c] == ".":
        i -= 1
    count += int(grid[i, c] == "#")

    # DOWN
    i = r + 1
    while grid[i, c] == ".":
        i += 1
    count += int(grid[i, c] == "#")

    # LEFT
    i = c - 1
    while grid[r, i] == ".":
        i -= 1
    count += int(grid[r, i] == "#")

    # RIGHT
    i = c + 1
    while grid[r, i] == ".":
        i += 1
    count += int(grid[r, i] == "#")

    # UP-LEFT
    i = r - 1
    j = c - 1
    while grid[i, j] == ".":
        i -= 1
        j -= 1
    count += int(grid[i, j] == "#")

    # UP-RIGHT
    i = r - 1
    j = c + 1
    while grid[i, j] == ".":
        i -= 1
        j += 1
    count += int(grid[i, j] == "#")

    # DOWN-LEFT
    i = r + 1
    j = c - 1
    while grid[i, j] == ".":
        i += 1
        j -= 1
    count += int(grid[i, j] == "#")

    # DOWN-RIGHT
    i = r + 1
    j = c + 1
    while grid[i, j] == ".":
        i += 1
        j += 1
    count += int(grid[i, j] == "#")

    return count


def iterate_v2(grid):
    new_grid = defaultdict(str)
    did_change = False

    for (r, c), state in list(grid.items()):
        if state == "L" and num_occupied_adjacent_seats_v2(grid, r, c) == 0:
            new_grid[r, c] = "#"
            did_change = True
        elif state == "#" and num_occupied_adjacent_seats_v2(grid, r, c) >= 5:
            new_grid[r, c] = "L"
            did_change = True
        else:
            new_grid[r, c] = grid[r, c]

    return new_grid, did_change


def main():
    with open("input.txt", "r") as fp:
        original_grid = defaultdict(str)
        for r, line in enumerate(fp):
            for c, char in enumerate(line.strip()):
                original_grid[r, c] = char

    grid = original_grid

    did_change = True
    while did_change:
        grid, did_change = iterate(grid)

    num_occupied = len(list(filter(lambda x: x == "#", grid.values())))

    print("Part I:", num_occupied)

    grid = original_grid

    did_change = True
    while did_change:
        grid, did_change = iterate_v2(grid)

    num_occupied = len(list(filter(lambda x: x == "#", grid.values())))

    print("Part II:", num_occupied)


if __name__ == "__main__":
    main()
