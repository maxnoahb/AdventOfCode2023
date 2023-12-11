def parse_input():
    lines = open("inputs/day9_input.txt").read().splitlines()
    histories = [list(map(int, l.split())) for l in lines]
    return histories


def find_differences(history):
    diff_list = [history]
    while True:
        cur_list = diff_list[-1]
        if all(i == 0 for i in cur_list):
            break
        diff_list.append([y - x for x, y, in zip(cur_list[0::], cur_list[1::])])
    return diff_list


def extrapolate(diff_list):
    reversed_list = diff_list[::-1]
    for x, y in zip(reversed_list[0::], reversed_list[1::]):
        y.append(x[-1] + y[-1])
    return reversed_list


def solve_part1(histories):
    final_sum = 0
    for history in histories:
        diff_list = find_differences(history)
        reversed_list = extrapolate(diff_list)
        final_sum += reversed_list[-1][-1]
    print(final_sum)


if __name__ == "__main__":
    histories = parse_input()
    solve_part1(histories)
