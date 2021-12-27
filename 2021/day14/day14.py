from collections import defaultdict
from copy import deepcopy


def apply_insertions(polymer, templates, steps):
    pairs = defaultdict(int)
    counts = defaultdict(int)
    for i in range(len(polymer) - 1):
        pairs[polymer[i : i + 2]] += 1

    for c in polymer:
        counts[c] += 1

    for _ in range(steps):
        pairs, counts = _apply_insertions(pairs, counts, templates)

    sorted_counts = sorted(counts.items(), key=lambda t: t[1])
    return sorted_counts[-1][1] - sorted_counts[0][1]


def _apply_insertions(pairs, counts, templates):
    new_pairs = deepcopy(pairs)
    new_counts = deepcopy(counts)

    for p in pairs:
        if p in templates:
            v = templates[p]
            new_pairs[p[0] + v] += pairs[p]
            new_pairs[v + p[1]] += pairs[p]
            new_pairs[p] -= pairs[p]
            new_counts[v] += pairs[p]

    return new_pairs, new_counts


def main():
    def parse_template(s):
        a, b = s.strip().split(" -> ")
        return a, b

    with open("input.txt", "r") as fp:
        polymer = fp.readline().strip()
        fp.readline()

        templates = list(map(parse_template, fp.readlines()))
        templates = {t[0]: t[1] for t in templates}

    print(apply_insertions(polymer, templates, 10))
    print(apply_insertions(polymer, templates, 40))


if __name__ == "__main__":
    main()
