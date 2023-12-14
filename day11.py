import numpy as np
from itertools import combinations


def parse_input():
    """Parse input text into list of list of chars and convert to numpy 2D array"""
    lines = open("inputs/day11_input.txt").read().splitlines()
    image = [list(i) for i in lines]
    return np.array(image)


def find_empty_rows_cols(image):
    """Return a list of the indices for entirely empty rows and columns with no # symbol"""
    empty_rows = [i for i, row in enumerate(image) if "#" not in row]
    empty_cols = [i for i, row in enumerate(zip(*image)) if "#" not in row]
    return empty_rows, empty_cols


def find_galaxies(image):
    """Return a list of coordinates for each # symbol"""
    galaxies_array = np.where(image == "#")
    return list(zip(galaxies_array[0], galaxies_array[1]))


def find_distance(x, y):
    """Find the shortest distance between two coordinates"""
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def solve(image, rows_to_expand):
    """
    Loop through all possible sets of two galaxies
    For each one, find the original distance between the two points, and then
        loop through our list of empty rows and columns
    Add the necessary amount of empty rows (1 for part 1, 999,999 for part 2)
        to the distance, then add that to the running sum of total distances
    """
    empty_rows, empty_cols = find_empty_rows_cols(image)
    galaxy_coords = find_galaxies(image)

    final_sum = 0
    for x, y in combinations(galaxy_coords, 2):
        dist = find_distance(x, y)
        x_row, x_col, y_row, y_col = x[0], x[1], y[0], y[1]
        for i in empty_rows:
            if x_row < i < y_row or y_row < i < x_row:
                dist += rows_to_expand - 1
        for j in empty_cols:
            if x_col < j < y_col or y_col < j < x_col:
                dist += rows_to_expand - 1

        final_sum += dist

    print(final_sum)


if __name__ == "__main__":
    image = parse_input()
    solve(image, rows_to_expand=2)
    solve(image, rows_to_expand=1000000)
