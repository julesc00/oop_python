import copy
import random


SUIT_TUPLE = ("Spades", "Hearts", "Clubs", "Diamonds")
RANK_TUPLE = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")
N_CARDS = 8

CARDS = [
    {"rank": "King", "suit": "Clubs", "value": 13},
]


def main():
    print("Welcome to Higher or Lower")
    print("You have to choose whether the next card to be shown will be higher or lower than the current card.")
    print("Right card = 20 points, Wrong card = -15 points")
    print("You have 50 points to start!")
    import pdb
    pdb.set_trace()
    starting_deck_list = []
    for suit in SUIT_TUPLE:
        for this_value, rank in enumerate(RANK_TUPLE):
            card_dict = {"rank": rank, "suit": suit, "value": this_value+1}
            starting_deck_list.append(card_dict)

    score = 50
    while True:
        print()
        game_deck_list = shuffle(starting_deck_list)

        current_card_dict = get_card(game_deck_list)
        current_card_rank = current_card_dict.get("rank")
        current_card_value = current_card_dict.get("value")
        current_card_suit = current_card_dict.get("suit")

        print(f"Starting card is: {current_card_rank} of {current_card_suit}")
        for card_number in range(0, N_CARDS):
            answer = input(
                f"""
                Will the next card be higher or lower than the {current_card_rank} or {current_card_suit}?
                Enter h or l
                """
            ).casefold()
            next_card_dict = get_card(game_deck_list)
            next_card_rank = next_card_dict.get("rank")
            next_card_suit = next_card_dict.get("suit")
            next_card_value = next_card_dict.get("value")
            print(f"Next card is {next_card_rank} of {next_card_suit}")

            if answer == "h":
                if next_card_value > current_card_value:
                    print("You got it right, it was higher!")
                    score += 20
                else:
                    print("Sorry, it was higher")
                    score -= 15
            elif answer == "l":
                if next_card_value < current_card_value:
                    score += 20
                    print("You got it right, it was lower")
                else:
                    score -= 15
                    print("Sorry, it was lower")

            print("Your score is:", score)
            print()
            current_card_rank = next_card_rank
            current_card_value = next_card_value

        go_again = input(f"To play again press ENTER or 'q' to quit: ").casefold()
        if go_again == "q":
            break
    print("Okay, bye")


def get_card(deck_list):
    this_card = deck_list.pop()
    return this_card


def shuffle(deck_list):
    deck_list_out = copy.deepcopy(deck_list)
    random.shuffle(deck_list_out)
    return deck_list_out


if __name__ == "__main__":
    main()
