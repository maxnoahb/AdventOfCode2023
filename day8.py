from ast import literal_eval


def parse_input():
    """Parse input into"""
    lines = open("inputs/day8_input.txt").read().strip().splitlines()
    lr_instructions = lines[0]
    nodes = {}
    for l in lines[2:]:
        split = l.split(" = ")
        node = split[0]
        lr = split[1].replace("(", "").replace(")", "").split(", ")
        nodes[node] = lr

    return lr_instructions, nodes


def solve_part1(lr_instructions, nodes):
    cur = "AAA"
    i = 0
    num_steps = 0
    while cur != "ZZZ":
        if lr_instructions[i] == "L":
            cur = nodes[cur][0]
        elif lr_instructions[i] == "R":
            cur = nodes[cur][1]
        i = i + 1 if i < (len(lr_instructions) - 1) else 0
        num_steps += 1

    print(num_steps)


if __name__ == "__main__":
    lr_instructions, nodes = parse_input()
    solve_part1(lr_instructions, nodes)
