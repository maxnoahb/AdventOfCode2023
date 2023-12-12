import math

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
    # print(lines)
    tiles = [list(i) for i in lines]
    # print(tiles)
    return tiles


def are_connected(x, y, dir, tiles):
    x_row, x_col = x
    y_row, y_col = y
    connected = False
    if 0 <= y_row < len(tiles) and 0 <= y_col < len(tiles[y_row]):
        x_val = tiles[x_row][x_col]
        y_val = tiles[y_row][y_col]
        if y_val in POSSIBLE_CONNECTIONS[x_val][dir]:
            connected = True
        # print(connected)
    return connected


def find_start(tiles):
    return next(
        (row, col)
        for row, row_val in enumerate(tiles)
        for col, col_val in enumerate(row_val)
        if col_val == "S"
    )


def solve_part1(tiles):
    current_tile = find_start(tiles)
    seen_tiles = [current_tile]
    path = [current_tile]
    count_tiles = 0
    while True:
        for dir, (x, y) in DIRS.items():
            next_tile = (current_tile[0] + x, current_tile[1] + y)
            if next_tile not in seen_tiles:
                # print(current_tile, next_tile, dir)
                if are_connected(current_tile, next_tile, dir, tiles):
                    # print("connected")
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


if __name__ == "__main__":
    tiles = parse_input()
    solve_part1(tiles)
    # are_connected((2, 0), (3, 0), "S", tiles)
    # are_connected((1, 0), (2, 0), "S", tiles)
    # are_connected((4, 0), (4, 1), "E", tiles)
    # are_connected((4, 1), (4, 0), "W", tiles)
    # are_connected((4, 1), (4, 2), "E", tiles)
