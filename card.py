class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank}-{self.suit}"

    @property
    def value(self) -> int:
        if self.rank == "A":
            value = 11
        elif self.rank in ["J", "Q", "K"]:
            value = 10
        else:
            value = int(self.rank)
        return value

    @staticmethod
    def hide(hand=None):
        if hand is None:
            hand = []
        ascii_cards = []
        for idx, card in enumerate(hand):
            suits = {"♥": "hearts", "♠": "spades", "♣": "clubs", "♦": "diamonds"}
            sign = [*{k for k, v in suits.items() if v == card.suit}]
            if idx == 0:
                ascii_cards.append(
                    [
                        "┌────────┐",
                        "│░░░░░░░░│",
                        "│░░░░░░░░│",
                        "│░░░░░░░░│",
                        "│░░░░░░░░│",
                        "│░░░░░░░░│",
                        "└────────┘",
                    ]
                )
            else:
                if card.rank != "10":
                    ascii_cards.append(
                        [
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
                    ascii_cards.append(
                        [
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

    @staticmethod
    def show(hand=None):
        if hand is None:
            hand = []
        ascii_cards = []
        for card in hand:
            suits = {"♥": "hearts", "♠": "spades", "♣": "clubs", "♦": "diamonds"}
            sign = [*{k for k, v in suits.items() if v == card.suit}]
            if card.rank != "10":
                ascii_cards.append(
                    [
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
                ascii_cards.append(
                    [
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
