from card import Card
from deck import Deck

deck = Deck()
deck.add_cards()
one_card = deck.cards.pop()


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.hand_value = 0

    def add_to_hand_value(self, value):
        self.hand_value = value

    def reset(self):
        self.hand = []
        self.hand_value = 0

    def add_card(self, card):
        self.hand.append(card)
        self.hand_value += card.value

    def show_hand(self):
        [print(*i) for i in zip(*Card.show(self.hand))]


class BlackJackPlayer(Player):
    def __init__(self, name, funds):
        super().__init__(name)
        self.funds = funds

    def add_funds(self, amount):
        if amount >= 0:
            self.funds += amount
        else:
            raise ValueError('the addFunds method must be passed a number greater than or equal to zero')

    def remove_funds(self, amount):
        if amount >= 0:
            self.funds -= amount
        else:
            raise ValueError('the removeFunds method must be passed a number greater than or equal to zero')

    def show_over_view(self):
        print(f"""┌────────────────────────────────{'─' * 15}┐
    \r│  Name: {self.name}  Hand-Total: {self.hand_value}  Balance: {self.funds}    │
    \r└────────────────────────────────{'─' * 15}┘""")


player = BlackJackPlayer('hasan', 1000)

print(player.hand_value)
print(player.funds)

player.show_over_view()
