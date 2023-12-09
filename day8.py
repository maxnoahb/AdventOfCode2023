import math


def parse_input():
    """
    Parse input into a string containing the left-right instructions, and a dict with format
        {
            "AAA": ["BBB", "CCC"],
            "BBB": ["ZZZ", "ABC"]
        }
    """
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
    """
    Loop until we hit a ZZZ node, resetting the node on each loop to the proper new node
    Increase the index of the left-right instructions on each loop and keep a running count of steps
    """
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


def solve_part2(lr_instructions, nodes):
    """
    Identify each node we want to start from, then loop through those nodes
    For each node to track, follow similar logic to part 1 to find the number of steps
        it takes until we reach a node ending in a Z
    Append to a list that keeps the number of steps necessary for each node,
        then find the LCM (least common multiple) of the list
    """
    nodes_to_track = [i for i in list(nodes.keys()) if i[-1] == "A"]
    steps = []
    for node in nodes_to_track:
        i = 0
        num_steps = 0
        while node[2] != "Z":
            if lr_instructions[i] == "L":
                node = nodes[node][0]
            elif lr_instructions[i] == "R":
                node = nodes[node][1]
            num_steps += 1
            i = i + 1 if i < (len(lr_instructions) - 1) else 0
        steps.append(num_steps)

    print(steps, math.lcm(*steps))


if __name__ == "__main__":
    lr_instructions, nodes = parse_input()
    solve_part1(lr_instructions, nodes)
    solve_part2(lr_instructions, nodes)
