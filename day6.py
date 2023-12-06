import re


def parse_input():
    with open("inputs/day6_input.txt", "r") as f:
        times, distances = f.readline().split()[1:], f.readline().split()[1:]
    return times, distances


def solve_part1(times, distances):
    final_product = 1
    for i in range(len(times)):
        options = 0
        race_time = int(times[i])
        distance = int(distances[i])
        # print(race_time, distance)
        for held_time in range(1, race_time):
            # print(held_time, (race_time - held_time) * held_time)
            if (race_time - held_time) * held_time > distance:
                options += 1
        final_product *= options
    print(final_product)


if __name__ == "__main__":
    times, distances = parse_input()
    solve_part1(times, distances)
