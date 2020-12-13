def terminates(instructions):
    curr_instruction = 0
    accumulator = 0
    executed = set()

    while True:
        if curr_instruction in executed:
            return False, accumulator

        if curr_instruction == len(instructions):
            return True, accumulator

        executed.add(curr_instruction)

        inst = instructions[curr_instruction]
        if inst[0] == "acc":
            curr_instruction += 1
            accumulator += inst[1]
        elif inst[0] == "nop":
            curr_instruction += 1
        else:
            curr_instruction += inst[1]


def main():
    with open("input.txt", "r") as fp:
        lines = [line.strip().split(" ") for line in fp]

    instructions = [[line[0], int(line[1])] for line in lines]

    executed = set()
    accumulator = 0
    curr_instruction = 0

    while True:
        if curr_instruction in executed:
            break

        executed.add(curr_instruction)

        inst = instructions[curr_instruction]
        if inst[0] == "acc":
            accumulator += inst[1]
            curr_instruction += 1
        elif inst[0] == "nop":
            curr_instruction += 1
        else:
            curr_instruction += inst[1]

    print("Part I:", accumulator)

    acc = None

    for i in executed:
        instruction = instructions[i]
        if instruction[0] == "nop":
            instruction[0] = "jmp"

            terminated, acc = terminates(instructions)
            if terminated:
                break

            instruction[0] = "nop"
        elif instruction[0] == "jmp":
            instruction[0] = "nop"

            terminated, acc = terminates(instructions)
            if terminated:
                break

            instruction[0] = "jmp"

    print("Part II:", acc)


if __name__ == "__main__":
    main()
