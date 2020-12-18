from operator import add, mul


def get_operator(token):
    return {"+": add, "*": mul}.get(token)


def evaluate_expression(expression):
    expression = list(expression.replace(" ", ""))

    def convert_int(c):
        if c in {"+", "*", "(", ")"}:
            return c

        return int(c)

    expression = list(map(convert_int, expression))

    parentheses_inds = []

    i = 0
    while i < len(expression):
        if expression[i] == "(":
            parentheses_inds.append(i)
            del expression[i]
        elif expression[i] == ")":
            reduce_range(expression, parentheses_inds[-1], i - 1)
            i -= i - 1 - parentheses_inds[-1]
            del expression[i]
            parentheses_inds.pop()
        else:
            i += 1

    reduce_range(expression, 0, len(expression) - 1)

    return expression[0]


def reduce_range(expression, low, high):
    acc = expression[low]
    i = low + 1

    while i < high:
        acc = get_operator(expression[i])(acc, expression[i + 1])
        i += 2

    del expression[low + 1 : high + 1]
    expression[low] = acc


def main():
    with open("input.txt", "r") as fp:
        expression_strings = [line.strip() for line in fp]

    results = [evaluate_expression(e) for e in expression_strings]

    print("Part I:", sum(results))


if __name__ == "__main__":
    main()
