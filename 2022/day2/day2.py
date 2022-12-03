from enum import Enum, auto
from functools import total_ordering


@total_ordering
class Shape(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    @classmethod
    def from_letter(cls, letter):
        if letter in {"A", "X"}:
            return Shape.ROCK

        if letter in {"B", "Y"}:
            return Shape.PAPER

        if letter in {"C", "Z"}:
            return Shape.SCISSORS

        raise NotImplementedError

    @classmethod
    def from_outcome(cls, opponent_letter, outcome_letter):
        opponent_shape = Shape.from_letter(opponent_letter)

        if outcome_letter == "X":
            # LOSE
            for s in Shape:
                if s < opponent_shape:
                    return s

            raise RuntimeError

        if outcome_letter == "Y":
            # DRAW
            return opponent_shape

        if outcome_letter == "Z":
            # WIN
            for s in Shape:
                if s > opponent_shape:
                    return s

            raise RuntimeError

        raise NotImplementedError

    @property
    def score(self):
        return {
            Shape.ROCK: 1,
            Shape.PAPER: 2,
            Shape.SCISSORS: 3,
        }[self]

    def __lt__(self, other):
        if self.__class__ is not other.__class__:
            raise NotImplementedError

        if self == Shape.ROCK:
            return other == Shape.PAPER

        if self == Shape.PAPER:
            return other == Shape.SCISSORS

        if self == Shape.SCISSORS:
            return other == Shape.ROCK


def score_round(opponent_shape: Shape, our_shape: Shape) -> int:
    if our_shape > opponent_shape:
        return 6 + our_shape.score

    if opponent_shape > our_shape:
        return our_shape.score

    return 3 + our_shape.score


def main():
    opponent_moves = []
    our_moves = []

    with open("input.txt", "r") as fp:
        for line in fp.readlines():
            a, b = line.strip().split(" ")
            opponent_moves.append(a)
            our_moves.append(b)

    total_score = sum(
        [
            score_round(Shape.from_letter(a), Shape.from_letter(b))
            for a, b in zip(opponent_moves, our_moves)
        ]
    )

    print(total_score)

    total_score = sum(
        [
            score_round(Shape.from_letter(a), Shape.from_outcome(a, b))
            for a, b in zip(opponent_moves, our_moves)
        ]
    )

    print(total_score)


if __name__ == "__main__":
    main()
