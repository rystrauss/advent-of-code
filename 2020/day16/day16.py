import itertools

import numpy as np


def main():
    with open("input.txt", "r") as fp:
        rules = dict()

        line = fp.readline()
        while line != "\n":
            name, ranges = line.strip().split(":")

            ranges = ranges.split(" or ")
            ranges = [r.split("-") for r in ranges]
            ranges = map(lambda t: range(int(t[0]), int(t[1]) + 1), ranges)
            valid_values = set.union(*map(set, ranges))

            rules[name] = valid_values

            line = fp.readline()

        fp.readline()

        our_ticket = list(map(int, fp.readline().strip().split(",")))

        fp.readline()
        fp.readline()

        nearby_tickets = []
        for line in fp.readlines():
            nearby_tickets.append(list(map(int, line.strip().split(","))))

    # Part I
    all_valid_values = set.union(*rules.values())
    error_rate = 0

    for i in itertools.chain(*nearby_tickets):
        if i not in all_valid_values:
            error_rate += i

    print("Part I:", error_rate)

    # Part II
    valid_tickets = []
    for ticket in nearby_tickets:
        is_valid = all([i in all_valid_values for i in ticket])
        if is_valid:
            valid_tickets.append(ticket)

    merged_tickets = list(map(set, zip(*valid_tickets, our_ticket)))

    num_fields = len(merged_tickets)

    possible_assignments = np.zeros((num_fields, num_fields), dtype=np.int8)

    for i in range(num_fields):
        for j, valid_values in enumerate(rules.values()):
            if merged_tickets[i].issubset(valid_values):
                possible_assignments[i, j] = 1

    while np.sum(possible_assignments) != -num_fields:
        col = np.argwhere(np.sum(possible_assignments, axis=0) == 1)[0, 0]
        row = np.argwhere(possible_assignments[:, col] == 1)[0, 0]
        possible_assignments[row, np.arange(num_fields) != col] = 0
        possible_assignments[row, col] = -1

    rule_names = list(rules.keys())
    departure_rules = np.array(
        [i for i in range(num_fields) if "departure" in rule_names[i]]
    )
    departure_fields = np.array(
        [np.argmin(possible_assignments[:, i]) for i in departure_rules]
    )

    answer = np.prod(np.array(our_ticket)[departure_fields])

    print("Part II:", answer)


if __name__ == "__main__":
    main()
