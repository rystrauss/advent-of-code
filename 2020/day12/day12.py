import math


def rotate(vector, degrees):
    sd = math.sin(math.radians(degrees))
    cd = math.cos(math.radians(degrees))
    x = vector[0]
    y = vector[1]

    vector[0] = cd * x - sd * y
    vector[1] = sd * x + cd * y


def main():
    with open("input.txt", "r") as fp:
        instructions = [line.strip() for line in fp]

    instructions = [(x[0], int(x[1:])) for x in instructions]

    pos = [0, 0]
    angle = 0

    for command, arg in instructions:
        if command == "N":
            pos[1] += arg
        elif command == "S":
            pos[1] -= arg
        elif command == "E":
            pos[0] += arg
        elif command == "W":
            pos[0] -= arg
        elif command == "L":
            angle += arg
        elif command == "R":
            angle -= arg
        else:
            pos[1] += math.sin(math.radians(angle)) * arg
            pos[0] += math.cos(math.radians(angle)) * arg

    print("Part I:", round(abs(pos[0]) + abs(pos[1])))

    pos = [0, 0]
    waypoint_pos = [10, 1]

    for command, arg in instructions:

        if command == "N":
            waypoint_pos[1] += arg
        elif command == "S":
            waypoint_pos[1] -= arg
        elif command == "E":
            waypoint_pos[0] += arg
        elif command == "W":
            waypoint_pos[0] -= arg
        elif command == "L":
            rotate(waypoint_pos, arg)
        elif command == "R":
            rotate(waypoint_pos, -arg)
        else:
            pos[1] += waypoint_pos[1] * arg
            pos[0] += waypoint_pos[0] * arg

    print("Part II:", round(abs(pos[0]) + abs(pos[1])))


if __name__ == "__main__":
    main()
