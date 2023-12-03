MAX = {"red": 12, "green": 13, "blue": 14}


def parse_input():
    with open("day2_input.txt", "r") as f:
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
    sum = 0
    for id, game in input_dict.items():
        possible = True
        for color in list(game.keys()):
            if game[color] > MAX[color]:
                possible = False
        if possible:
            sum += id
    print(sum)


if __name__ == "__main__":
    input_dict = parse_input()
    solve_part1(input_dict)
