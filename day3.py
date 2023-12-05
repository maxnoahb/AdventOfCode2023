import re


def parse_input():
    """
    Read input file and store data for matches for symbols and numbers
    Output format:
        {
            (1,3): "*",
            (4,27): "/"
        }
    """
    with open("inputs/day3_input.txt", "r") as f:
        lines = f.read().splitlines()
    symbol_coords = []
    number_coords = []
    for row, line in enumerate(lines):
        symbol_matches = [
            {(row, match.start()): match.group()} for match in re.finditer("[^\.\d]", line)
        ]
        number_matches = [
            {(row, match.start()): int(match.group())} for match in re.finditer("\d", line)
        ]
        symbol_coords.extend(symbol_matches)
        number_coords.extend(number_matches)
    return symbol_coords, number_coords


def find_symbol_adjacent_coords():
    """
    Generate a list of all adjacent coordinates for all symbols
    For gear symbols specifically, create a dict with key of the symbol coordinates
        and value of the list of adjacent coordinates, because we will need to track
        how many adjacent numbers there are for each gear
    """
    symbol_coords, number_coords = parse_input()
    symbol_coords_list = [list(k.keys())[0] for k in symbol_coords]
    adjacent_coords = []
    gear_adjacent_coords = {}
    for coords in symbol_coords_list:
        gear_adjacent_coords[coords] = []
        x, y = coords[0], coords[1]
        for row_diff in [-1, 0, 1]:
            for col_diff in [-1, 0, 1]:
                adjacent_coords.append((x + row_diff, y + col_diff))
                symbol = next(d for d in symbol_coords if list(d.keys())[0] == coords)[coords]
                if symbol == "*":
                    gear_adjacent_coords[coords].append((x + row_diff, y + col_diff))
    adjacent_coords = [x for x in adjacent_coords if x not in symbol_coords_list]
    gear_adjacent_coords = {
        k: [v1 for v1 in v if v1 != k] for k, v in gear_adjacent_coords.items() if v != []
    }
    return symbol_coords, number_coords, adjacent_coords, gear_adjacent_coords


def find_previous_numbers(x, y, number, number_coords, number_coords_list, seen_coords):
    """
    Given that we have found a digit at a coordinate adjacent to a symbol, check whether
        the char immediately to the left is also a number, and concatenate if so
    """
    next_coords = (x, y + 1)
    while next_coords in number_coords_list:
        if next_coords in seen_coords:
            break
        else:
            px, py = next_coords[0], next_coords[1]
            next_number = next(d for d in number_coords if list(d.keys())[0] == next_coords)[
                next_coords
            ]
            number = str(number) + str(next_number)
            seen_coords.append(next_coords)
            next_coords = (px, py + 1)
    return number, seen_coords


def find_next_numbers(x, y, number, number_coords, number_coords_list, seen_coords):
    """
    Given that we have found a digit at a coordinate adjacent to a symbol, check whether
        the char immediately to the right is also a number, and concatenate if so
    """
    previous_coords = (x, y - 1)
    while previous_coords in number_coords_list:
        if previous_coords in seen_coords:
            break
        else:
            px, py = previous_coords[0], previous_coords[1]
            previous_number = next(
                d for d in number_coords if list(d.keys())[0] == previous_coords
            )[previous_coords]
            number = str(previous_number) + str(number)
            seen_coords.append(previous_coords)
            previous_coords = (px, py - 1)
    return number, seen_coords


def solve_part1():
    """
    Keep a running list of all coordinates we have seen already, to avoid duplicating.
    Loop through the list of all coordinates adjacent to a symbol, and if we have not seen it
        check whether it is a digit.
    If it's a digit, find any digits to the right or left to get the full number,
        then add it to the final sum.
    """
    _, number_coords, adjacent_coords, _ = find_symbol_adjacent_coords()
    number_coords_list = [list(k.keys())[0] for k in number_coords]
    seen_coords = []
    final_sum = 0
    for coords in adjacent_coords:
        if coords not in seen_coords:
            if coords in number_coords_list:
                seen_coords.append(coords)
                x, y = coords[0], coords[1]
                number = next(d for d in number_coords if list(d.keys())[0] == coords)[coords]
                number, seen_coords = find_previous_numbers(
                    x, y, number, number_coords, number_coords_list, seen_coords
                )
                number, seen_coords = find_next_numbers(
                    x, y, number, number_coords, number_coords_list, seen_coords
                )
                final_sum += int(number)
    print(final_sum)


def solve_part2():
    """
    Keep a running list of all coordinates we have seen already, to avoid duplicating.
    Also keep a list of unique numbers adjacent to each gear.
    Loop through the list of all coordinates adjacent to a gear, and if we have not seen it
        check whether it is a digit.
    If it's a digit, find any digits to the right or left to get the full number.
    After looping through all coordinates, if there are exactly two numbers in the unique list,
        then multiply then and add to the running sum.
    """
    _, number_coords, _, gear_adjacent_coords = find_symbol_adjacent_coords()
    number_coords_list = [list(k.keys())[0] for k in number_coords]
    seen_coords = []
    final_sum = 0
    for gear_coords, adjacent_coords in gear_adjacent_coords.items():
        unique_numbers = []
        for coords in adjacent_coords:
            if coords not in seen_coords:
                if coords in number_coords_list:
                    seen_coords.append(coords)
                    x, y = coords[0], coords[1]
                    number = next(d for d in number_coords if list(d.keys())[0] == coords)[coords]
                    number, seen_coords = find_previous_numbers(
                        x, y, number, number_coords, number_coords_list, seen_coords
                    )
                    number, seen_coords = find_next_numbers(
                        x, y, number, number_coords, number_coords_list, seen_coords
                    )
                    unique_numbers.append(int(number))

        if len(unique_numbers) == 2:
            product = unique_numbers[0] * unique_numbers[1]
            final_sum += product

    print(final_sum)


if __name__ == "__main__":
    solve_part1()
    solve_part2()
