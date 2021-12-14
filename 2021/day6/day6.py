from copy import copy


def simulate(fish, n):
    fish = copy(fish)

    for _ in range(n):
        new_fish, *fish = fish
        fish.append(new_fish)
        fish[6] += new_fish

    return sum(fish)


def main():
    with open("input.txt", "r") as fp:
        initial_fish = list(map(int, fp.readline().strip().split(",")))

    fish = [0] * 9

    for i in initial_fish:
        fish[i] += 1

    print(simulate(fish, 80))
    print(simulate(fish, 256))


if __name__ == "__main__":
    main()
