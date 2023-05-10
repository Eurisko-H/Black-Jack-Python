from deck import Deck


def test_add_card_length():
    deck = Deck()
    deck.add_cards()
    assert len(deck.cards) == 52


def test_add_card_value():
    deck = Deck()
    deck.add_cards()
    assert deck.cards[-1].value == 11


def test_add_card_type():
    deck = Deck()
    deck.add_cards()
    assert deck.cards[-1].rank == "A"
