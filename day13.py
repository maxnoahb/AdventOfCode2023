def parse_input():
    """Parse input into a list of lists with a line for each row in each grid"""
    return [grid.splitlines() for grid in open("inputs/day13_input.txt").read().split("\n\n")]


def difference(seq1, seq2):
    """Given two strings, return the number of chars that differ between them"""
    return sum(1 for a, b in zip(seq1, seq2) if a != b)


def find_reflection(grid, smudges):
    """
    Given a grid (list of strings, with each string being a row), loop through indices
    Create a zipped list with the remaining rows beginning at that index, and the reversed list
        of rows before the index (e.g. "abcdef" at index 3: compare "def" to "cba")
    If there is a valid reflection, these lists should match
    Also take an argument smudges (defaulted to 0) for an optional number of
        differences to match between the lists if not looking for a perfect reflection
    """
    for i in range(1, len(grid)):
        zipped_list = list(zip(grid[i:], grid[:i][::-1]))
        if sum(difference(a, b) for a, b in zipped_list) == smudges:
            return i
    return 0


def solve(smudges=0):
    """
    Loop through all grids, looking for a reflection across rows in each
    To find reflections across columns, simply transpose the list of lists and repeat
    Add to the running score total as instructed
    """
    grids = parse_input()
    score = 0
    for grid in grids:
        reflection_horizontal = find_reflection(grid, smudges)
        score += reflection_horizontal * 100
        reflection_vertical = find_reflection(list(zip(*grid)), smudges)
        score += reflection_vertical
    print(score)


if __name__ == "__main__":
    solve()
    solve(smudges=1)
