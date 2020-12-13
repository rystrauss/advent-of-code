def required_bags(rules, bag):
    inside_bags = rules[bag]

    if not inside_bags:
        return 0

    return sum([required_bags(rules, b[0]) * b[1] for b in inside_bags]) + sum(
        [b[1] for b in inside_bags]
    )


def main():
    with open("input.txt", "r") as fp:
        lines = fp.readlines()

    # Part I
    rules = {"shiny gold": set()}
    for line in lines:
        head, tail = line.split(" contain ")

        outer = head[:-5]
        inners = tail[:-1].split(", ")
        inners = [" ".join(c.split(" ")[1:-1]) for c in inners]

        for bag in inners:
            rules.setdefault(bag, set()).add(outer)

    visited = set()
    to_visit = set(rules["shiny gold"])

    while to_visit:
        next_color = to_visit.pop()
        visited.add(next_color)
        expanded = rules.get(next_color)
        if expanded is None:
            continue
        to_visit.update(expanded)

    print("Part I:", len(visited))

    # Part II
    rules = dict()
    for line in lines:
        head, tail = line.split(" contain ")

        outer = head[:-5]
        inners = tail[:-1].split(", ")
        inners = [c.split(" ")[:-1] for c in inners]

        if inners[0][0] == "no":
            inners = []
        else:
            inners = [(" ".join(x[1:]), int(x[0])) for x in inners]

        rules[outer] = inners

    print("Part II:", required_bags(rules, "shiny gold"))


if __name__ == "__main__":
    main()
