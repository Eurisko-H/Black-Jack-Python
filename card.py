class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

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
