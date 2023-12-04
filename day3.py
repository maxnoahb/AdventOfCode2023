import re


def parse_input():
    with open("inputs/day3_input.txt", "r") as f:
        lines = f.read().splitlines()
    symbol_coords = []
    number_coords = []
    for row, line in enumerate(lines):
        # print(row, line)
        symbol_matches = [(row, match.start()) for match in re.finditer("[^\.\d]", line)]
        number_matches = [
            {(row, match.start()): int(match.group())} for match in re.finditer("\d", line)
        ]
        # print(symbol_matches)
        symbol_coords.extend(symbol_matches)
        number_coords.extend(number_matches)
        # print(number_matches)
    return symbol_coords, number_coords


def find_symbol_adjacent_coords():
    symbol_coords, number_coords = parse_input()
    # print(symbol_coords)
    # print(number_coords)
    adjacent_coords = []
    for coords in symbol_coords:
        x, y = coords[0], coords[1]
        for row_diff in [-1, 0, 1]:
            for col_diff in [-1, 0, 1]:
                adjacent_coords.append((x + row_diff, y + col_diff))
        adjacent_coords.remove(coords)
    return symbol_coords, number_coords, adjacent_coords


def find_numbers():
    _, number_coords, adjacent_coords = find_symbol_adjacent_coords()
    # print(adjacent_coords)
    number_coords_list = [list(k.keys())[0] for k in number_coords]
    seen_coords = []
    final_sum = 0
    for coords in adjacent_coords:
        if coords not in seen_coords:
            if coords in number_coords_list:
                seen_coords.append(coords)
                x, y = coords[0], coords[1]
                number = next(d for d in number_coords if list(d.keys())[0] == coords)[coords]
                # print("number", number)
                previous_coords = (x, y - 1)
                while previous_coords in number_coords_list:
                    if previous_coords not in seen_coords:
                        px, py = previous_coords[0], previous_coords[1]
                        previous_number = next(
                            d for d in number_coords if list(d.keys())[0] == previous_coords
                        )[previous_coords]
                        # print("previous_number", previous_number)
                        number = str(previous_number) + str(number)
                        seen_coords.append(previous_coords)
                        previous_coords = (px, py - 1)
                    else:
                        break
                next_coords = (x, y + 1)
                while next_coords in number_coords_list:
                    if next_coords not in seen_coords:
                        px, py = next_coords[0], next_coords[1]
                        next_number = next(
                            d for d in number_coords if list(d.keys())[0] == next_coords
                        )[next_coords]
                        # print("next_number", next_number)
                        number = str(number) + str(next_number)
                        seen_coords.append(next_coords)
                        next_coords = (px, py + 1)
                    else:
                        break
                # print(coords)
                # print("cats", number)
                final_sum += int(number)
    print(final_sum)


if __name__ == "__main__":
    find_numbers()
