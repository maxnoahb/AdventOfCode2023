import re
from num2words import num2words
from word2number import w2n


def read_file_to_list(file):
    with open(file, "r") as f:
        text = f.read()
    string_list = text.splitlines()
    return string_list


def sum_values(string_list, regex_pattern):
    sum = 0
    for s in string_list:
        matches = re.findall(regex_pattern, s)
        value = matches[0] + matches[-1]
        sum += int(value)
    return sum


def solve_part1():
    string_list = read_file_to_list("day1_input.txt")
    sum = sum_values(string_list, "\d")
    print(sum)


def solve_part2():
    string_list = read_file_to_list("day1_input.txt")
    digits = [num2words(i) for i in list(range(1, 10))]
    digits.append("\d")
    combined_regex = "(?=(" + ")|(".join(digits) + "))"
    sum = 0
    for s in string_list:
        matches = ["".join(i) for i in re.findall(combined_regex, s)]
        matches = [str(w2n.word_to_num(i)) for i in matches]
        value = matches[0] + matches[-1]
        sum += int(value)
    print(sum)


if __name__ == "__main__":
    solve_part1()
    solve_part2()
