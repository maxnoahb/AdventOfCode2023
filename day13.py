def parse_input():
    grids = [grid.splitlines() for grid in open("inputs/day13_input.txt").read().split("\n\n")]
    return grids


def find_reflection(grid):
    for i in range(1, len(grid)):
        # print("i", i)
        # print(grid[i:], "cats", grid[:i][::-1])
        # print(grid[i:] == grid[:i][::-1])
        zipped_list = list(zip(grid[i:], grid[:i][::-1]))
        # print(zipped_list)
        if all(l == r for l, r in zipped_list):
            return i
        # for l, r in zip(grid[i:], grid[:i][::-1]):
        #     print(all(l == r))
    # print(reflections)
    return 0


def solve():
    grids = parse_input()
    score = 0
    for grid in grids:
        reflection_horizontal = find_reflection(grid)
        # print(reflection_horizontal)
        score += reflection_horizontal * 100
        reflection_vertical = find_reflection(list(zip(*grid)))
        # print(reflection_vertical)
        score += reflection_vertical
    print(score)


if __name__ == "__main__":
    solve()
