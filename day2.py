from functools import reduce
import operator

MAX = {"red": 12, "green": 13, "blue": 14}


def parse_input():
    """
    Input format:
        Game 1: 8 green; 5 green, 6 blue, 1 red; 2 green, 1 blue, 4 red
        Game 2: 10 blue, 12 red; 8 red; 7 green, 5 red, 7 blue
    Output format: (take the highest value for each color in each game)
        {
            1: {
                "green": 8,
                "blue": 6,
                "red": 4
            },
            2: {
                "blue": 10,
                "red": 12,
                "green": 7
            }
        }
    """
    with open("inputs/day2_input.txt", "r") as f:
        input_list = f.read().splitlines()
    input_dict = {}
    count = 1
    for i in input_list:
        input_dict[count] = {}
        game = i.split(":")[1].split(";")
        for cube_set in game:
            cube_list = cube_set.strip().split(", ")
            for cubes in cube_list:
                split = cubes.split(" ")
                color = split[1]
                number = split[0]
                if int(number) > int(input_dict[count].get(color, 0)):
                    input_dict[count][color] = int(number)
        count += 1
    return input_dict


def solve_part1(input_dict):
    cubes = 0
    for id, game in input_dict.items():
        possible = True
        for color in list(game.keys()):
            if game[color] > MAX[color]:
                possible = False
        if possible:
            cubes += id
    print(cubes)


def solve_part2(input_dict):
    cubes = 0
    for _, game in input_dict.items():
        num_cubes = reduce(operator.mul, game.values())
        cubes += num_cubes
    print(cubes)


if __name__ == "__main__":
    input_dict = parse_input()
    solve_part1(input_dict)
    solve_part2(input_dict)
