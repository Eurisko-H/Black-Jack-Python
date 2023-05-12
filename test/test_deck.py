from deck import Deck
import pytest


@pytest.fixture()
def deck_instance():
    return Deck.add_cards()


def test_add_card_length(deck_instance):
    assert len(deck_instance) == 52


def test_add_card_value(deck_instance):
    assert deck_instance[-1].value == 11


def test_add_card_type(deck_instance):
    assert deck_instance[-1].rank == "A"
