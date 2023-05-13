import random

from card import Card
from deck import Deck


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.hand_value = 0
        self.aces = 0

    def reset(self):
        self.hand = []
        self.hand_value = 0
        self.aces = 0

    def add_card(self, card):
        self.hand.append(card)
        self.hand_value += card.value
        if card.rank == "A":
            self.aces += 1

    def adjust_for_ace(self):
        while self.hand_value > 21 and self.aces >= 1:
            self.hand_value -= 10
            self.aces -= 1

    def show_hand(self):
        [print(*i) for i in zip(*Card.show(self.hand))]


class BlackJackPlayer(Player):
    def __init__(self, name, funds):
        super().__init__(name)
        self.funds = funds
        self.bet = 0

    def add_funds(self, amount: int):
        if amount >= 0:
            self.funds += amount
        else:
            raise ValueError('the addFunds method must be passed a number greater than or equal to zero')

    def remove_funds(self, amount: int):
        if amount >= 0:
            self.funds -= amount
        else:
            raise ValueError('the removeFunds method must be passed a number greater than or equal to zero')

    def show_over_view(self):
        print(f"""┌────────────────────────────────{'─' * 20}┐
                \r│  Name: {self.name}  Hand-Total: {self.hand_value}  Balance: {self.funds}         │
                \r└────────────────────────────────{'─' * 20}┘""")


class BlackJackDealer(Player, Deck):
    def __init__(self, name):
        super().__init__(name)
        self.black_jack_deck = Deck.add_cards()

    def reset_deck(self):
        self.black_jack_deck = Deck.add_cards()

    def shuffle_cards(self):
        random.shuffle(self.black_jack_deck)

    def show_hand_cover(self):
        [print(*i) for i in zip(*Card.hide(self.hand))]

    def deal(self):
        return self.black_jack_deck.pop()

    def show_over_view(self, show_value):
        if show_value:
            print(f"""┌────────────────────────────────{'─' * 4}┐
                \r│  Name: {self.name}  Hand-Total: {self.hand_value}      │
                \r└────────────────────────────────{'─' * 4}┘""")
        else:
            print(f"""┌────────────────────────────────{'─' * 4}┐
                \r│  Name: {self.name}  Hand-Total: {"?"}       │
                \r└────────────────────────────────{'─' * 4}┘""")
