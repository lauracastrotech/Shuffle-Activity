from random import randint

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♣"]

deck_of_cards = [f"{card}{suit}" for card in CARDS for suit in SUITS]

def shuffle_deck(deck_of_cards):
    print(f"{deck_of_cards=}")
    for card in range(len(deck_of_cards)):
        random_card = randint(0, len(deck_of_cards) - 1)

        current_card = deck_of_cards[card]

        deck_of_cards[card] = deck_of_cards[random_card]

        deck_of_cards[random_card] = current_card
    return deck_of_cards
    
print(shuffle_deck(deck_of_cards))