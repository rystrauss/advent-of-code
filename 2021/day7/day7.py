import numpy as np


def main():
    with open("input.txt", "r") as fp:
        nums = list(map(int, fp.readline().strip().split(",")))

    nums = np.array(nums)

    def calculate_cost(i):
        return np.sum(np.abs(nums - i))

    calculate_cost = np.vectorize(calculate_cost)

    costs = calculate_cost(np.arange(nums.min(), nums.max() + 1))

    print(costs.min())

    def calculate_growing_cost(i):
        d = np.abs(nums - i)
        c = d * (d + 1) / 2
        return np.sum(c)

    calculate_growing_cost = np.vectorize(calculate_growing_cost)

    costs = calculate_growing_cost(np.arange(nums.min(), nums.max() + 1))

    print(costs.min())


if __name__ == "__main__":
    main()
