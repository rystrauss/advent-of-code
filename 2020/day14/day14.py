def padded_binary(num, length=36):
    binary_value = bin(num).removeprefix("0b")
    return "0" * (length - len(binary_value)) + binary_value


class Memory:
    def __init__(self):
        self._mask = "X" * 36
        self._data = dict()

    def __setitem__(self, key, value):
        binary_value = padded_binary(value)
        masked_binary_value = self._apply_mask(binary_value)
        self._data[key] = int(masked_binary_value, 2)

    def _apply_mask(self, binary_value):
        masked_value = []

        for i, m in zip(binary_value, self._mask):
            if m == "X":
                masked_value.append(i)
            else:
                masked_value.append(m)

        return "".join(masked_value)

    def get_sum(self):
        return sum(self._data.values())

    def set_mask(self, new_mask):
        self._mask = new_mask


class MemoryV2:
    def __init__(self):
        self._mask = "X" * 36
        self._data = dict()

    def __setitem__(self, key, value):
        for address in self._get_addresses(padded_binary(key)):
            self._data[address] = value

    def _get_addresses(self, binary_address):
        floating_indices = []
        masked_address = []

        for i, (j, m) in enumerate(zip(binary_address, self._mask)):
            if m == "0":
                masked_address.append(j)
            elif m == "1":
                masked_address.append("1")
            else:
                masked_address.append("X")
                floating_indices.append(i)
        for i in range(2 ** len(floating_indices)):
            b = padded_binary(i, len(floating_indices))
            for j, k in zip(floating_indices, b):
                masked_address[j] = k
            yield "".join(masked_address)

    def get_sum(self):
        return sum(self._data.values())

    def set_mask(self, new_mask):
        self._mask = new_mask


def execute(memory, instructions):
    for inst in instructions:
        command, arg = inst.split(" = ")

        if command == "mask":
            memory.set_mask(arg)
        else:
            key = int(command[4:-1])
            memory[key] = int(arg)


def main():
    with open("input.txt", "r") as fp:
        instructions = [line.strip() for line in fp]

    mem = Memory()
    execute(mem, instructions)
    print("Part I:", mem.get_sum())

    mem = MemoryV2()
    execute(mem, instructions)
    print("Part II:", mem.get_sum())


if __name__ == "__main__":
    main()
