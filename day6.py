import re


def parse_input():
    """Parse input into two lists, one of times and one of distances"""
    with open("inputs/day6_input.txt", "r") as f:
        times, distances = f.readline().split()[1:], f.readline().split()[1:]
    return times, distances


def solve_part1(times, distances):
    """
    Loop through each game, storing the time and distance for each.
    Then loop through each possible time for holding the button, and calculate
        the theoretical distance with (race_time - held_time) * held_time.
    Keep a sum of the options for winning hold times, and multiply to the running product
    """
    final_product = 1
    for i in range(len(times)):
        options = 0
        race_time = int(times[i])
        distance = int(distances[i])
        for held_time in range(1, race_time):
            if (race_time - held_time) * held_time > distance:
                options += 1
        final_product *= options
    print(final_product)


def solve_part2(times, distances):
    """
    Follow the same logic as part 1, but considering the whole line as one number
        and forgoing the initial loop
    """
    race_time = int("".join(times))
    distance = int("".join(distances))
    options = 0
    for held_time in range(1, race_time):
        if (race_time - held_time) * held_time > distance:
            options += 1
    print(options)


if __name__ == "__main__":
    times, distances = parse_input()
    solve_part1(times, distances)
    solve_part2(times, distances)
