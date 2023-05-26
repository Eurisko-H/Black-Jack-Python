import itertools
from card import Card


class Deck:
    @staticmethod
    def add_cards():
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["spades", "clubs", "hearts", "diamonds"]
        black_jack_deck = itertools.product(ranks, suits)
        return [Card(rank, suit) for rank, suit in black_jack_deck]
