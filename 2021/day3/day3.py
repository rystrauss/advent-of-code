import numpy as np


def main():

    with open("input.txt", "r") as fp:
        bits = fp.readlines()

    bits = [list(x.strip()) for x in bits]
    bits = np.array(bits, dtype=int)

    gamma = np.median(bits, axis=0).astype(int)
    epsilon = 1 - gamma

    coefs = np.flip(2 ** np.arange(gamma.shape[0], dtype=int))
    gamma = np.sum(gamma * coefs)
    epsilon = np.sum(epsilon * coefs)

    print(gamma * epsilon)

    oxy_values = np.ma.masked_array(bits, mask=[[False]])

    index = 0
    while True:
        most_common = np.ceil(np.ma.median(oxy_values, axis=0)[index]).astype(int)
        invalid_inds = oxy_values[:, index] != most_common
        oxy_values[invalid_inds, :] = np.ma.masked

        valid_inds = np.where(~oxy_values.mask[:, index])[0]
        if len(valid_inds) == 1:
            oxy_rating = np.sum(bits[valid_inds[0]] * coefs)
            break

        index += 1

    co2_values = np.ma.masked_array(bits, mask=[[False]])

    index = 0
    while True:
        most_common = np.ceil(np.ma.median(co2_values, axis=0)[index]).astype(int)
        invalid_inds = co2_values[:, index] == most_common
        co2_values[invalid_inds, :] = np.ma.masked

        valid_inds = np.where(~co2_values.mask[:, index])[0]
        if len(valid_inds) == 1:
            co2_rating = np.sum(bits[valid_inds[0]] * coefs)
            break

        index += 1

    print(oxy_rating * co2_rating)


if __name__ == "__main__":
    main()
