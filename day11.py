import numpy as np
from itertools import combinations


def parse_input():
    lines = open("inputs/day11_input.txt").read().splitlines()
    # print(lines)
    image = [list(i) for i in lines]
    # print(image)
    return image


def find_empty_rows_cols(image):
    empty_rows = [i for i, row in enumerate(image) if "#" not in row]
    empty_cols = [i for i, row in enumerate(zip(*image)) if "#" not in row]
    # print(empty_rows)
    # print(empty_cols)
    # print(len(image))
    # print(len(image[0]))
    # print(image)
    count_row_loops = 0
    for row in empty_rows:
        image.insert(row + count_row_loops, ["."] * len(image[0]))
        count_row_loops += 1
    count_col_loops = 0
    for col in empty_cols:
        for row in image:
            row.insert(col + count_col_loops, ".")
        count_col_loops += 1
    # print(len(image))
    # print(len(image[0]))
    # print(image)
    return np.array(image)


def find_galaxies(image):
    galaxies_array = np.where(image == "#")
    return list(zip(galaxies_array[0], galaxies_array[1]))


def find_distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def solve_part1(image):
    image = find_empty_rows_cols(image)
    galaxy_coords = find_galaxies(image)

    final_sum = 0
    for combo in combinations(galaxy_coords, 2):
        # print(combo)
        dist = find_distance(combo[0], combo[1])
        # print(dist)
        final_sum += dist

    print(final_sum)


if __name__ == "__main__":
    image = parse_input()
    solve_part1(image)
