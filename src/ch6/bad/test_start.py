import pytest
from cards import Card, InvalidCardId


@pytest.mark.smok
@pytest.mark.exception
def test_start_non_existent(cards_db):
    any_number = 123
    with pytest.raises(InvalidCardId):
        cards_db.start(any_number)