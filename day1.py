import re


def solve():
    with open("day1_input.txt", "r") as f:
        text = f.read()
    string_list = text.splitlines()

    sum = 0
    for s in string_list:
        matches = re.findall("\d", s)
        value = matches[0] + matches[-1]
        sum += int(value)

    print(sum)


if __name__ == "__main__":
    solve()
