import math


def check_time(x, matching_index, bus_ids, offsets):
    for i, d in zip(bus_ids[matching_index:], offsets[matching_index:]):
        if (x + d) % i != 0:
            return matching_index
        matching_index += 1
    return matching_index


def main():
    with open("input.txt", "r") as fp:
        earliest_depart_time = int(fp.readline())
        bus_ids = fp.readline().strip().split(",")
        bus_schedule = {int(j): i for i, j in enumerate(bus_ids) if j != "x"}
        bus_ids = list(bus_schedule.keys())

    departure_time = earliest_depart_time
    winning_bus_id = None

    while True:
        for i in bus_ids:
            if departure_time % i == 0:
                winning_bus_id = i
                break
        else:
            departure_time += 1
            continue
        break

    print("Part I:", (departure_time - earliest_depart_time) * winning_bus_id)

    buses = sorted(bus_schedule.items(), key=lambda x: x[0], reverse=True)

    bus_ids, offsets = zip(*buses)

    matching_index = 0
    x = 0

    while True:
        matching_index = check_time(x, matching_index, bus_ids, offsets)
        if matching_index == len(bus_ids):
            break
        x += math.prod(bus_ids[:matching_index])

    print("Part II:", x)


if __name__ == "__main__":
    main()
