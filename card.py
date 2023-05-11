class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank}-{self.suit}"

    def rank(self):
        return self.rank

    def suit(self):
        return self.suit

    @property
    def value(self):
        if self.rank == "A":
            value = 11
        elif self.rank in ['J', 'Q', 'K']:
            value = 10
        else:
            value = int(self.rank)
        return value

    @staticmethod
    def show(hand=None):
        if hand is None:
            hand = []
        ascii_cards = []
        for card in hand:
            suits = {"♥": 'hearts', "♠": 'spades', "♣": 'clubs', "♦": 'diamonds'}
            sign = [*{k for k, v in suits.items() if v == card.suit}]
            if card.rank != "10":
                ascii_cards.append([
                    "┌────────┐",
                    f"│{card.rank}       │",
                    "│        │",
                    f"│   {sign[0]}    │",
                    "│        │",
                    f"│       {card.rank}│",
                    "└────────┘",
                ]
                )
            else:
                ascii_cards.append([
                    "┌────────┐",
                    f"│{card.rank}      │",
                    "│        │",
                    f"│   {sign[0]}    │",
                    "│        │",
                    f"│      {card.rank}│",
                    "└────────┘",
                ]
                )
        return ascii_cards
