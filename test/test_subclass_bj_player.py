import pytest
from player import BlackJackPlayer


@pytest.fixture
def player_instance():
    player = BlackJackPlayer('hasan', 1000)
    return player


def test_add_funds(player_instance):
    player_instance.add_funds(200)
    assert player_instance.funds == 1200


def test_add_funds_raise_error(player_instance):
    with pytest.raises(ValueError) as exc_info:
        player_instance.add_funds(-100)
    assert str(exc_info.value) == 'the addFunds method must be passed a number greater than or equal to zero'


def test_remove_funds(player_instance):
    player_instance.remove_funds(500)
    assert player_instance.funds == 500


def test_remove_funds_raise_error(player_instance):
    with pytest.raises(ValueError,
                       match='the removeFunds method must be passed a number greater than or equal to zero'):
        player_instance.remove_funds(-10)
