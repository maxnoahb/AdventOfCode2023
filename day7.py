card_values = {str(i): i for i in range(2, 10)}
card_values.update({"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14})


def parse_input():
    """Parse input into a dict of format {hand_string: bid}"""
    lines = open("inputs/day7_input.txt").read().strip().splitlines()
    hands = {l.split(" ")[0]: l.split(" ")[1] for l in lines}
    return hands


def eval_hand(hand, joker):
    """
    Find the ranking of a hand, according to the given possibilities:
        7. Five of a kind
        6. Four of a kind
        5. Full house
        4. Three of a kind
        3. Two pairs
        2. One pair
        1. High card
    Do this by creating a sorted list of the count of each card in the hand
    """
    card_count = sorted([hand.count(i) for i in set(hand)])

    # if Js are jokers instead of jacks, remove the jokers and then add the
    # number of jokers to the highest card count
    if joker:
        count_j = hand.count("J")
        if 0 < count_j < 5:
            card_count.remove(count_j)
            card_count[-1] += count_j

    if card_count == [5]:
        return 7
    elif card_count == [1, 4]:
        return 6
    elif card_count == [2, 3]:
        return 5
    elif card_count == [1, 1, 3]:
        return 4
    elif card_count == [1, 2, 2]:
        return 3
    elif card_count == [1, 1, 1, 2]:
        return 2
    else:
        return 1


def score_hands(hands, joker):
    """
    Loop through all hands and store data for each (score, a tuple of the card values, the bid)
    Store all of this as a list of tuples so we can easily sort it (sort by score first,
        then by card value as a tiebreaker)
    """
    scored_hands = []
    for hand, bid in hands.items():
        hand_value = eval_hand(hand, joker)
        card_value_tuple = tuple(card_values[c] for c in hand)
        scored_hands.append((hand_value, card_value_tuple, int(bid)))

    return scored_hands


def solve_part1(hands):
    """
    Once we have the list of tuples, loop through and find the value for each by
        multiplying the ranking by the bid. Add to running sum
    """
    scored_hands = score_hands(hands, joker=False)
    final_score = 0
    for index, (_, _, bid) in enumerate(sorted(scored_hands)):
        score = bid * (index + 1)
        final_score += score

    print(final_score)


def solve_part2(hands):
    """
    Follow the same process but taking jokers into account
    """
    card_values["J"] = 1
    scored_hands = score_hands(hands, joker=True)
    final_score = 0
    for index, (_, _, bid) in enumerate(sorted(scored_hands)):
        score = bid * (index + 1)
        final_score += score

    print(final_score)


if __name__ == "__main__":
    hands = parse_input()
    solve_part1(hands)
    solve_part2(hands)
