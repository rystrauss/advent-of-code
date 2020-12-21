import regex


def solve(rules, strings):
    def expand(pattern):
        if not pattern.isnumeric():
            return pattern

        return f"(?:{''.join(map(expand, rules[pattern].split()))})"

    r = regex.compile(expand("0"))
    return sum(r.fullmatch(s) is not None for s in strings)


def main():
    with open("input.txt", "r") as fp:
        rule_strings = []
        line = fp.readline()
        while line != "\n":
            rule_strings.append(line.strip())
            line = fp.readline()

        messages = [line.strip() for line in fp]

    rules = dict()
    for s in rule_strings:
        id, rule = s.split(": ")
        rules[id] = rule.strip('"')

    print("Part I:", solve(rules, messages))

    rules["8"] = "42 +"
    rules["11"] = "(?P<R> 42 (?&R)? 31 )"

    print("Part II:", solve(rules, messages))


if __name__ == "__main__":
    main()
