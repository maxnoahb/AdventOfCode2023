import math

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""
DIRS = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
POSSIBLE_CONNECTIONS = {
    "|": {"N": ["|", "7", "F", "S"], "E": [], "S": ["|", "L", "J", "S"], "W": []},
    "-": {"N": [], "E": ["-", "J", "7", "S"], "S": [], "W": ["-", "L", "F", "S"]},
    "L": {"N": ["|", "7", "F", "S"], "E": ["-", "J", "7", "S"], "S": [], "W": []},
    "J": {"N": ["|", "7", "F", "S"], "E": [], "S": [], "W": ["-", "L", "F", "S"]},
    "7": {"N": [], "E": [], "S": ["|", "L", "J", "S"], "W": ["-", "L", "F", "S"]},
    "F": {"N": [], "E": ["-", "J", "7", "S"], "S": ["|", "L", "J", "S"], "W": []},
    ".": {"N": [], "E": [], "S": [], "W": []},
    "S": {"N": ["|", "7", "F"], "E": ["-", "J", "7"], "S": ["|", "L", "J"], "W": ["-", "L", "F"]},
}


def parse_input():
    lines = open("inputs/day10_input.txt").read().splitlines()
    return [list(i) for i in lines]


def are_connected(x, y, dir, tiles):
    """
    Given two coordinates, a direction (N/E/S/W), and the full list of tiles,
    determine whether the coordinates are a valid connection per the lookup dict
    """
    x_row, x_col = x
    y_row, y_col = y
    connected = False

    # ensure the coordinates are within the boundaries
    if 0 <= y_row < len(tiles) and 0 <= y_col < len(tiles[y_row]):
        x_val = tiles[x_row][x_col]
        y_val = tiles[y_row][y_col]
        if y_val in POSSIBLE_CONNECTIONS[x_val][dir]:
            connected = True

    return connected


def find_start(tiles):
    """Return the (x,y) coordinates of the lone S tile in the list of tiles"""
    return next(
        (row, col)
        for row, row_val in enumerate(tiles)
        for col, col_val in enumerate(row_val)
        if col_val == "S"
    )


def solve_part1(tiles):
    """
    Traverse the path with a loop. Begin at the S tile after we find its location
    Keep a running list of tiles we have seen, and also the tiles belonging in the path
    At each point, loop through the four possible directions (N,E,S,W) and find the coordinates
        for each; if we haven't seen this tile yet, then check if the next tile and current tile
        are a valid connection per our lookup dict; if so, consider it part of the path and then
        continue the loop from that tile
    Break out of the loop after we have considered all tiles
    Print the length of the path divided in half, to find the furthest number of tiles away
    """
    current_tile = find_start(tiles)
    seen_tiles = [current_tile]
    path = [current_tile]
    count_tiles = 0
    while True:
        for dir, (x, y) in DIRS.items():
            next_tile = (current_tile[0] + x, current_tile[1] + y)
            if next_tile not in seen_tiles:
                if are_connected(current_tile, next_tile, dir, tiles):
                    seen_tiles.append(next_tile)
                    path.append(next_tile)
                    count_tiles += 1
                    current_tile = next_tile
                    break
            else:
                continue
        else:
            break

    print(math.ceil(count_tiles / 2))
    return path


def find_area(path):
    """
    Use the Shoelace formula to find the area of a polygon using a list of all its points
    https://en.wikipedia.org/wiki/Shoelace_formula
    First add the start point of the path to the end of the list, so we end at the same point
    """
    path_copy = path
    path_copy.append(path[0])
    return (
        sum(
            row1 * col2 - row2 * col1
            for (row1, col1), (row2, col2) in zip(path_copy, path_copy[1:])
        )
        / 2
    )


def find_interior_points(path, area):
    """
    Use Pick's theorem to find the number of points within a polygon, given the number of
        interior points (via the Shoelace formula) and the number of boundary points
    https://en.wikipedia.org/wiki/Pick%27s_theorem
    """
    return int(abs(area) - (math.floor(len(path) / 2)) + 1)


def solve_part2(path):
    """
    Find the area of the polygon formed by the path with the Shoelace formula, then
        find the number of interior points with Pick's theorem

    Note: thanks to this writeup (https://advent-of-code.xavd.id/writeups/2023/day/10/)
        for the idea on using that formula and theorem. Was stuck on this one!
    """
    area = find_area(path)
    interior_points = find_interior_points(path, area)
    print(interior_points)


if __name__ == "__main__":
    tiles = parse_input()
    path = solve_part1(tiles)
    solve_part2(path)
