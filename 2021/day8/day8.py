import itertools
from collections import Counter

import ray
from ray.util.multiprocessing import Pool


def main():
    def parse_input_line(s):
        signals, output = s.strip().split(" | ")
        signals = signals.split()
        output = output.split()
        return signals, output

    with open("input.txt", "r") as fp:
        data = list(map(parse_input_line, fp.readlines()))

    def count_easy_digits(t):
        _, output = t

        counts = Counter(map(len, output))
        return counts[2] + counts[3] + counts[4] + counts[7]

    print(sum(map(count_easy_digits, data)))

    valid_signals = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9,
    }

    to_add = dict()

    for s, v in valid_signals.items():
        for p in itertools.permutations(s):
            to_add["".join(p)] = v

    valid_signals.update(to_add)

    def apply_mapping(s, permutation):
        mapping = {ord(a): ord(b) for a, b in zip(list("abcdefg"), permutation)}
        return s.translate(mapping)

    def compute_output(t):
        signals, output = t
        for p in itertools.permutations("abcdefg"):
            translated_signals = {apply_mapping(s, p) for s in signals}

            if translated_signals.issubset(valid_signals):
                decoded_output = [apply_mapping(s, p) for s in output]
                decoded_output = [str(valid_signals[s]) for s in decoded_output]
                decoded_output = int("".join(decoded_output))
                return decoded_output

        raise RuntimeError

    ray.init(num_cpus=12)
    pool = Pool()
    output_sum = 0

    for r in pool.map(compute_output, data):
        output_sum += r

    print(output_sum)

    ray.shutdown()


if __name__ == "__main__":
    main()
