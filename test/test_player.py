import pytest

from deck import Deck
from player import Player


@pytest.fixture
def player_instance():
    player = Player('hasan')
    black_jack_deck = Deck.add_cards()
    one_card = black_jack_deck.pop()
    second_card = black_jack_deck.pop()
    player.add_card(one_card)
    player.add_card(second_card)
    return player


def test_name(player_instance):
    assert player_instance.name == 'hasan'


def test_hand(player_instance):
    assert player_instance.hand[0].rank == "A"


def test_hand_value(player_instance):
    player_instance.hand_value = 110
    assert player_instance.hand_value == 110


def test_reset(player_instance):
    player_instance.reset()
    assert player_instance.hand == []
    assert player_instance.hand_value == 0
    assert player_instance.aces == 0


def test_adjust_ace(player_instance):
    player_instance.adjust_for_ace()
    assert player_instance.hand_value == 12
    assert player_instance.aces == 1


def test_ace_counter(player_instance):
    assert player_instance.aces == 2
