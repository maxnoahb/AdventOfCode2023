def parse_input():
    card_list = []
    with open("inputs/day4_input.txt", "r") as f:
        lines = f.read().splitlines()
    for l in lines:
        entry = {}
        pipe_split = l.split(":")[1].split("|")
        winning_number_list = list(filter(None, pipe_split[0].split(" ")))
        elf_number_list = list(filter(None, pipe_split[1].split(" ")))
        entry["winning_number_list"] = winning_number_list
        entry["elf_number_list"] = elf_number_list
        card_list.append(entry)
    return card_list


def solve_part1(card_list):
    final_sum = 0
    for card in card_list:
        wins = card["winning_number_list"]
        elf = card["elf_number_list"]
        winning_number_count = sum(x in wins for x in elf)
        # print(winning_number_count)
        score = 2 ** (winning_number_count - 1)
        # print("score", score)
        final_sum += int(score)
    print(final_sum)


if __name__ == "__main__":
    card_list = parse_input()
    solve_part1(card_list)
