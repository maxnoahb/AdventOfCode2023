card_values = {str(i): i for i in range(2, 10)}
card_values.update({"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14})


def parse_input():
    lines = open("inputs/day7_input.txt").read().strip().splitlines()
    hands = {l.split(" ")[0]: l.split(" ")[1] for l in lines}
    return hands


def eval_hand(hand):
    card_count = sorted([hand.count(i) for i in set(hand)])
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


def solve_part1(hands):
    scored_hands = []
    for hand, bid in hands.items():
        # print(hand)
        hand_value = eval_hand(hand)
        # print(hand_value)
        card_value_tuple = tuple(card_values[c] for c in hand)
        # print(card_value_tuple)
        scored_hands.append((hand_value, card_value_tuple, int(bid)))

    final_score = 0
    for index, (hand_value, card_value_tuple, bid) in enumerate(sorted(scored_hands)):
        print(index + 1, hand_value, card_value_tuple, bid)
        score = bid * (index + 1)
        final_score += score

    print(final_score)


if __name__ == "__main__":
    hands = parse_input()
    solve_part1(hands)
