def main():
    with open("input.txt", "r") as fp:
        buffer = fp.read().strip()

    for i in range(4, len(buffer)):
        if len(set(buffer[i - 4 : i])) == 4:
            print(i)
            break

    for i in range(14, len(buffer)):
        if len(set(buffer[i - 14 : i])) == 14:
            print(i)
            break


if __name__ == "__main__":
    main()
