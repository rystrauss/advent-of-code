import numpy as np
from numpy.lib import stride_tricks


def main():
    depths = np.loadtxt("input.txt", dtype=int)

    delta = depths[1:] - depths[:-1]
    did_increase = delta > 0
    num_increases = np.count_nonzero(did_increase)
    print(num_increases)

    windows = stride_tricks.sliding_window_view(depths, 3)
    window_sums = np.sum(windows, axis=-1)
    delta = window_sums[1:] - window_sums[:-1]
    did_increase = delta > 0
    num_increases = np.count_nonzero(did_increase)
    print(num_increases)


if __name__ == "__main__":
    main()
