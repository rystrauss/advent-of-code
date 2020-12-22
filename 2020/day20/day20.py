import numpy as np
import pickle
import os


SEA_MONSTER = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    ],
    dtype=np.bool,
)


def parse_tile(raw_tile):
    header, rows = raw_tile.split("\n", 1)
    tile_id = int(header[5:-1])
    tile_data = [[c == "#" for c in row] for row in rows.split("\n")]
    tile_data = np.array(tile_data, np.bool)
    return tile_id, tile_data


def transformations(tile):
    rot90 = np.rot90(tile, 1)
    rot180 = np.rot90(tile, 2)
    rot270 = np.rot90(tile, 3)
    return [
        tile,
        rot90,
        rot180,
        rot270,
        np.flip(tile, axis=0),
        np.flip(rot90, axis=0),
        np.flip(rot180, axis=0),
        np.flip(rot270, axis=0),
    ]


def can_place(image, tile, r, c):
    if r > 0:
        tile_above = image[r - 1, c][1]
        if not np.array_equal(tile_above[-1], tile[0]):
            return False
    if c > 0:
        tile_left = image[r, c - 1][1]
        if not np.array_equal(tile_left[:, -1], tile[:, 0]):
            return False

    return True


def build_image(tiles):
    if os.path.exists("arranged-tiles.pkl"):
        with open("arranged-tiles.pkl", "rb") as fp:
            return pickle.load(fp)

    print("Arranging tiles...")

    unplaced_tiles = set(tiles.keys())
    image = dict()
    n = int(np.sqrt(len(tiles)))

    def _build_image(pos):
        if pos == n ** 2:
            return True

        r = pos // n
        c = pos % n

        for tile_id in tiles.keys():
            if tile_id not in unplaced_tiles:
                continue

            for tile in transformations(tiles[tile_id]):
                if can_place(image, tile, r, c):
                    image[r, c] = (tile_id, tile)
                    unplaced_tiles.remove(tile_id)

                    if _build_image(pos + 1):
                        return True

                    del image[r, c]
                    unplaced_tiles.add(tile_id)

        return False

    _build_image(0)

    with open("arranged-tiles.pkl", "wb") as fp:
        pickle.dump(image, fp)

    return image


def glue_image(image):
    n = int(np.sqrt(len(image)))

    glued_rows = []

    for r in range(n):
        glued_rows.append(np.hstack([image[r, c][1][1:-1, 1:-1] for c in range(n)]))

    return np.vstack(glued_rows)


def get_monster_locations(image):
    h, w = SEA_MONSTER.shape
    n = image.shape[0]

    monster_locations = np.zeros_like(image)

    for image_view, monster_view in zip(
        transformations(image), transformations(monster_locations)
    ):
        for r in range(n - h):
            for c in range(n - w):
                if np.array_equal(
                    SEA_MONSTER, image_view[r : r + h, c : c + w] & SEA_MONSTER
                ):
                    monster_view[r : r + h, c : c + w] |= SEA_MONSTER

    return monster_locations


def main():
    with open("input.txt", "r") as fp:
        tiles = fp.read().strip().split("\n\n")

    tiles = dict(map(parse_tile, tiles))
    image = build_image(tiles)

    n = int(np.sqrt(len(tiles)))
    corner_product = np.prod(
        [
            image[0, 0][0],
            image[0, n - 1][0],
            image[n - 1, 0][0],
            image[n - 1, n - 1][0],
        ]
    )

    print("Part I:", corner_product)

    image = glue_image(image)
    monster_locations = get_monster_locations(image)
    water_roughness = np.count_nonzero(image) - np.count_nonzero(monster_locations)

    print("Part II:", water_roughness)


if __name__ == "__main__":
    main()
