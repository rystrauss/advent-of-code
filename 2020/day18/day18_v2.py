from functools import reduce
from operator import add


class CustomInt:
    def __init__(self, *args):
        self._int = int(*args)

    def __pow__(self, power):
        return CustomInt(self._int + power._int)

    def __add__(self, other):
        return CustomInt(self._int + other._int)

    def __mul__(self, other):
        return CustomInt(self._int * other._int)

    def __sub__(self, other):
        return CustomInt(self._int * other._int)

    def __str__(self):
        return str(self._int)


def convert_string(expression):
    expression = expression.replace(" ", "")
    expression = list(expression)
    converted_expression = []

    for t in expression:
        if t in {"(", ")", "**", "*", "+"}:
            converted_expression.append(t)
        else:
            converted_expression.append(f"CustomInt({t})")

    return "".join(converted_expression)


def main():
    with open("input.txt", "r") as fp:
        expression_strings = [line.strip() for line in fp]

    expression_strings = [convert_string(s) for s in expression_strings]

    expressions_part1 = map(lambda s: s.replace("*", "-"), expression_strings)
    results = [eval(s) for s in expressions_part1]
    print("Part I:", reduce(add, results, CustomInt(0)))

    expressions_part2 = map(lambda s: s.replace("+", "**"), expression_strings)
    results = [eval(s) for s in expressions_part2]
    print("Part II:", reduce(add, results, CustomInt(0)))


if __name__ == "__main__":
    main()
