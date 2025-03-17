from random import randint

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♣"]

deck_of_cards = [f"{card}{suit}" for card in CARDS for suit in SUITS]

# Implement a solution for shuffling a deck of cards
# Use only randint() and no other imports
def shuffle_deck(deck_of_cards):
    # Loop through deck
    for card in range(len(deck_of_cards)):
        random_card = randint(0, len(deck_of_cards) - 1)
        print(f"{random_card=}")
        print(f"{len(deck_of_cards)=}")
        current_card = deck_of_cards[card]
        deck_of_cards[card] = deck_of_cards[random_card]
        deck_of_cards[random_card] = current_card

    # Generate a random index
    # Assign current index to temp variable
    # Assign element at random index to current index
    # Assign temp variable to random index
shuffle_deck(deck_of_cards)