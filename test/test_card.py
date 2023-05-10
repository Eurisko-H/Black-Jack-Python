from card import Card


def test_rank():
    card = Card('Q', 'diamonds')
    assert card.rank == 'Q'


def test_suit():
    card = Card('K', 'clubs')
    assert card.suit == 'clubs'


def test_value_for_ace():
    card = Card('A', 'clubs')
    assert card.value == 11


def test_value_for_other():
    card = Card('7', 'clubs')
    assert card.value == 7


def test_value_for_q():
    card = Card('Q', 'hearts')
    assert card.value == 10
