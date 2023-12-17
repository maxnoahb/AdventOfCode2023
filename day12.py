from functools import cache


def parse_input():
    """Parse input into format [("???.###", (1,1,3)), (".??..??...?##.", (1,1,3))]"""
    lines = open("inputs/day12_input.txt").read().splitlines()
    inputs = [
        (row, tuple(map(int, groups.split(",")))) for row, groups in [l.split() for l in lines]
    ]
    return inputs


@cache
def find_all_solutions(row, groups):
    """
    Combine recursion and dynamic programming to approach the problem
    Read the string left to right, continuously making the string smaller while recursing
    Thanks to this write-up for the idea for the dynamic programming approach:
        https://advent-of-code.xavd.id/writeups/2023/day/12/
    """

    # if the string is now empty, the solution is possible if there are no more groups to consider
    if not row:
        return 1 if len(groups) == 0 else 0

    # if there are no more groups to consider, the solution is possible if there are no more #s
    if not groups:
        return 1 if "#" not in row else 0

    # split string into left-most char and the remaining string
    cur, rest = row[0], row[1:]

    # if the current char is a . then we can continue recursing because it is irrelevant
    if cur == ".":
        return find_all_solutions(rest, groups)
    # if it's a ? then we recurse with both possible values for the char (. and #)
    elif cur == "?":
        return find_all_solutions(f".{rest}", groups) + find_all_solutions(f"#{rest}", groups)
    # if it's a # then we need to look at a number of possibilities
    elif cur == "#":
        # the group to consider
        group = groups[0]
        row_length = len(row)
        if (
            # is the string a possible length for the group
            group <= row_length
            # is there a . character breaking up the group
            and "." not in row[:group]
            # are we either at the end of the string, or is there not a # extending the group
            and (row_length == group or row[group] != "#")
        ):
            # recurse by moving forward in the groups, and from the new point in the string
            return find_all_solutions(row[group + 1 :], groups[1:])
        return 0
    else:
        raise ValueError("Invalid character")


def solve(unfold=False):
    inputs = parse_input()
    final_sum = 0
    for row, groups in inputs:
        if unfold:
            groups *= 5
            row = "?".join([row] * 5)
        final_sum += find_all_solutions(row, groups)
    print(final_sum)


if __name__ == "__main__":
    solve()
    solve(unfold=True)
