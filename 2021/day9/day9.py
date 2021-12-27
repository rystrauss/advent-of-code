import math
from collections import defaultdict
from dataclasses import dataclass
from typing import Any, Optional

import numpy as np


class UnionFind:
    @dataclass
    class _Node:
        data: Any
        parent: Optional["UnionFind._Node"] = None
        size: int = 1
        rank: int = 0

    def __init__(self, elements):
        self._element_map = dict()

        for e in elements:
            self._element_map[e] = self._Node(e)

    def find(self, element):
        path = []
        current = self._element_map[element]

        while current.parent is not None:
            path.append(current)
            current = current.parent

        for n in path:
            n.parent = current

        return current.data

    def union(self, element1, element2):
        n1 = self._element_map[self.find(element1)]
        n2 = self._element_map[self.find(element2)]

        if n1 == n2:
            return

        if n1.rank >= n2.rank:
            n2.parent = n1
            n1.size += n2.size
            if n1.rank == n2.rank:
                n1.rank += 1
        else:
            n1.parent = n2
            n2.size += n1.size

    def get_set_sizes(self):
        representatives = set()

        for e in self._element_map.keys():
            rep = self.find(e)
            representatives.add(rep)

        return [self._element_map[r].size for r in representatives]


def local_minima(x):
    x = np.pad(x, 1, constant_values=np.iinfo(x.dtype).max)

    result = (
        (x < np.roll(x, -1, axis=0))
        & (x < np.roll(x, 1, axis=0))
        & (x < np.roll(x, -1, axis=1))
        & (x < np.roll(x, 1, axis=1))
    )

    return result[1:-1, 1:-1]


def main():
    with open("input.txt", "r") as fp:
        data = [list(map(int, line.strip())) for line in fp.readlines()]

    heights = np.array(data)

    low_points = local_minima(heights)
    risk_levels = (heights + 1) * low_points
    print(np.sum(risk_levels))

    elements = []

    for i in range(heights.shape[0]):
        for j in range(heights.shape[1]):
            if heights[i, j] == 9:
                continue

            elements.append((i, j))


    uf = UnionFind(elements)

    XDELTA = [1, 0]
    YDELTA = [0, 1]

    for i in range(heights.shape[0]):
        for j in range(heights.shape[1]):
            for k in range(len(XDELTA)):
                x = j + XDELTA[k]
                y = i + YDELTA[k]
                if (
                    y >= 0
                    and y < heights.shape[0]
                    and x < heights.shape[1]
                    and heights[i, j] != 9
                    and heights[y, x] != 9
                ):
                    uf.union((i, j), (y, x))

    sizes = list(sorted(uf.get_set_sizes()))
    print(math.prod(sizes[-3:]))



if __name__ == "__main__":
    main()
