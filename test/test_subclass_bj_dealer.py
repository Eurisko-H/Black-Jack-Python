import pytest
from player import BlackJackDealer


@pytest.fixture
def player_instance():
    dealer = BlackJackDealer('dealer')
    return dealer


def test_reset_deck(player_instance):
    player_instance.reset_deck()
    assert len(player_instance.black_jack_deck) == 52

