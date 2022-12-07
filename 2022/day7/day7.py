TOTAL_SPACE = 70000000
REQUIRED_FREE_SPACE = 30000000


def main():
    directory_sizes = {}
    cur_location = []
    last_command = None

    def lineage():
        yield "/"

        for i in range(len(cur_location)):
            yield "/" + "/".join(cur_location[: i + 1])

    with open("input.txt", "r") as fp:
        for line in fp.readlines():
            parts = line.strip().split(" ")

            if parts[0] == "$":
                if parts[1] == "cd":
                    if parts[2] == "..":
                        assert cur_location
                        cur_location.pop()
                    elif parts[2] == "/":
                        cur_location.clear()
                    else:
                        cur_location.append(parts[2])

                    last_command = "cd"
                elif parts[1] == "ls":
                    last_command = "ls"
                else:
                    raise RuntimeError
            elif last_command == "ls":
                if parts[0] != "dir":
                    for path in lineage():
                        directory_sizes.setdefault(path, 0)
                        directory_sizes[path] += int(parts[0])

    total = sum(filter(lambda i: i <= 100000, directory_sizes.values()))
    print(total)

    used_space = directory_sizes["/"]
    unused_space = TOTAL_SPACE - used_space
    need_to_free = REQUIRED_FREE_SPACE - unused_space

    size_to_free = min(filter(lambda i: i >= need_to_free, directory_sizes.values()))
    print(size_to_free)


if __name__ == "__main__":
    main()
