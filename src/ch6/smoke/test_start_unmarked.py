import pytest
from cards import Card, InvalidCardId


@pytest.mark.smoke
def test_start(cards_db):
    i = cards_db.add_card(Card('foo', state='todo'))
    cards_db.start(i)
    c = Cards_db.get_card(i)
    assert c.state == 'in prog'

def test_start_non_existent(cards_db):
    any_number = 123
    with pytest.raises(InvalidCardId):
        cards_db.start(any_number)

