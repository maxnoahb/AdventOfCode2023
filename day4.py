def parse_input():
    """
    Parse input file by line, creating a list of dicts for each card list:
    [
        {
            "winning_number_list": ["4", "16", "87"],
            "elf_number_list": ["54", "36", "14"]
        },
        etc
    ]
    """
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
    """
    Loop through each list entry, find how many numbers from the elf list are in
        the winning list, compute the score and add to a running sum
    """
    final_sum = 0
    for cards in card_list:
        wins = cards["winning_number_list"]
        elf = cards["elf_number_list"]
        win_count = sum(x in wins for x in elf)
        score = 2 ** (win_count - 1)
        final_sum += int(score)

    print(final_sum)


def solve_part2(card_list):
    """
    Create a dict to store the number of copies for each card.
    Loop through each list entry, find how many numbers from the elf list are in
        the winning list, then look up how many copies of the card we have.
    Update the dict with the proper number of copies for the proper number of
        succeeding cards, then sum the total cards
    """
    num_copies_dict = {i: 1 for i in range(1, len(card_list) + 1)}
    for i, cards in enumerate(card_list):
        card_number = i + 1
        wins = cards["winning_number_list"]
        elf = cards["elf_number_list"]
        win_count = sum(x in wins for x in elf)
        num_copies = num_copies_dict[card_number]
        for x in range(win_count):
            new_card_number = card_number + x + 1
            num_copies_dict[new_card_number] += num_copies

    print(sum(num_copies_dict.values()))


if __name__ == "__main__":
    card_list = parse_input()
    solve_part1(card_list)
    solve_part2(card_list)
