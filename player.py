from card import Card
from deck import Deck

deck = Deck()
deck.add_cards()
one_card = deck.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self._hand_value = 0

    def name(self):
        return self.name

    def hand(self):
        return self.hand

    @property
    def hand_value(self):
        return self._hand_value

    @hand_value.setter
    def hand_value(self, value):
        self._hand_value = value

    def reset(self):
        self.hand = []
        self.hand_value = 0

    def add_card(self, card):
        self.hand.append(card)
        self.hand_value += card.value

    def show_hand(self):
        [print(*i) for i in zip(*Card.show(self.hand))]


player = Player('hasan')
player.add_card(one_card)
player.show_hand()
