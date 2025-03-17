from random import randint

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♣"]

deck_of_cards = [f"{card}{suit}" for card in CARDS for suit in SUITS]

# Implement a solution for shuffling a deck of cards
# Use only randint() and no other imports
def shuffle_deck(deck_of_cards):  
    length = len(deck_of_cards)

    for i in range(length):
        random_index = randint(0, length - 1)
        # Pop the card at random index
        card = deck_of_cards.pop(random_index)
        # Append the deleted card to end of list to shuffle the order
        deck_of_cards.append(card)

    return deck_of_cards

# Deck of cards before shuffling
print(deck_of_cards)

# Deck of cards after shuffling
print(shuffle_deck(deck_of_cards))

# Keep in mind that there are algorithms that some built-in functions use for shuffling. Follow your curiosity!
