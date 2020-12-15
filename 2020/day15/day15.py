from collections import deque

STARTING_NUMBERS = [1, 0, 18, 10, 19, 6]


def main():
    memory = dict()

    turn = 0
    for i in STARTING_NUMBERS:
        memory.setdefault(i, deque([], maxlen=2)).append(turn)
        turn += 1

    prev_number = STARTING_NUMBERS[-1]
    while turn < 2020:
        history = memory[prev_number]
        if len(history) == 1:
            will_say = 0
        else:
            will_say = history[-1] - history[-2]
        memory.setdefault(will_say, deque([], maxlen=2)).append(turn)
        prev_number = will_say
        turn += 1

    print("Part I:", prev_number)

    while turn < 30_000_000:
        if turn % 5000000 == 0:
            print(f"On turn {turn}...")

        history = memory[prev_number]
        if len(history) == 1:
            will_say = 0
        else:
            will_say = history[-1] - history[-2]
        memory.setdefault(will_say, deque([], maxlen=2)).append(turn)
        prev_number = will_say
        turn += 1

    print("Part II:", prev_number)


if __name__ == "__main__":
    main()
