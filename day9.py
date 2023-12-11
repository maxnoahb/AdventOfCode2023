def parse_input():
    """Parse input data into a list of list of ints: [[0,1,2,3,4], [5,6,7,8,9]]"""
    lines = open("inputs/day9_input.txt").read().splitlines()
    histories = [list(map(int, l.split())) for l in lines]
    return histories


def find_differences(history):
    """
    Given a list of ints, create a new list by finding the difference between each
        number in the list
    Append this to the list of lists, and loop until all numbers in the list are 0
    Return the reversed list of lists (so we can extrapolate backwards)
    """
    diff_list = [history]
    while True:
        cur_list = diff_list[-1]
        if all(i == 0 for i in cur_list):
            break
        diff_list.append([y - x for x, y, in zip(cur_list[0::], cur_list[1::])])

    return diff_list[::-1]


def extrapolate(diff_list):
    """
    Given a list of list of ints, extrapolate the next value by appending onto each list
        the sum of the last value of the current and previous list
    Return the list of lists with the extrapolated values added
    """
    for x, y in zip(diff_list[0::], diff_list[1::]):
        y.append(x[-1] + y[-1])

    return diff_list


def solve(histories, reverse):
    """
    For each line with a history of values, find the differences, extrapolate the next value,
        then add the final extrapolated value (last value of last list) to a running sum
    For part 2, we just need to reverse the history list and repeat the process
    """
    final_sum = 0
    for history in histories:
        history = history[::-1] if reverse else history
        diff_list = find_differences(history)
        ext_list = extrapolate(diff_list)
        final_sum += ext_list[-1][-1]

    print(final_sum)


if __name__ == "__main__":
    histories = parse_input()
    # part 1
    solve(histories, reverse=False)
    # part 2
    solve(histories, reverse=True)
