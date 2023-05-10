import itertools
from card import Card


class Deck:
    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)

    def add_cards(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        black_jack_deck = itertools.product(ranks, suits)
        [self.cards.append(Card(rank, suit)) for rank, suit in black_jack_deck]


deck = Deck()
deck.add_cards()
print(deck.cards[-1].value)
