import numpy as np


def main():
    with open("input.txt", "r") as fp:
        numbers = list(map(int, fp.readline().strip().split(",")))
        fp.readline()
        boards = fp.read().strip().split("\n\n")

    def parse_board(s):
        rows = s.split("\n")
        board = [list(map(int, r.split())) for r in rows]
        return board

    boards = np.ma.masked_array(list(map(parse_board, boards)), [[[False]]])

    has_won = [False] * len(boards)

    for n in numbers:
        for i, board in enumerate(boards):
            row, col = np.where(board == n)

            if np.size(row) == 0:
                continue

            board[row, col] = np.ma.masked

            if not has_won[i] and (
                5 in np.sum(board.mask, axis=0) or 5 in np.sum(board.mask, axis=1)
            ):
                if sum(has_won) == 0:
                    print("First Winner:", np.ma.sum(board) * n)

                if sum(has_won) == len(has_won) - 1:
                    print("Last Winner:", np.ma.sum(board) * n)

                has_won[i] = True


if __name__ == "__main__":
    main()
