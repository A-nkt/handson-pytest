"""
Test Cases
* `list` from an empty database
* `list` from a non-empty database
"""
from cards import Card


def test_list_no_cards(cards_db):
    """Empty db, empty list"""
    assert cards_db.list_cards() == []


def test_list_several_cards(cards_db):
    """
    Given a variety of cards, make sure they get returned.
    """
    orig = [
        Card("foo"),
        Card("bar", owner="me"),
        Card("baz", owner="you", state="in prog"),
    ]

    for c in orig:
        cards_db.add_card(c)

    the_list = cards_db.list_cards()

    assert len(the_list) == len(orig)
    for c in orig:
        assert c in the_list


def test_one(cards_db):
    orig = [
        Card("foo"),
        Card("bar", owner="me"),
        Card("baz", owner="you", state="in prog"),
    ]

    for c in orig:
        cards_db.add_card(c)

    for c in orig:
        for c2 in cards_db.list_cards(owner=c.owner):
            assert c.owner == c2.owner


def test_two(cards_db):
    orig = [
        Card("foo"),
        Card("bar", owner="me"),
        Card("baz", owner="you", state="in prog"),
    ]

    for c in orig:
        cards_db.add_card(c)

    for c in orig:
        for c2 in cards_db.list_cards(state=c.state):
            assert c.state == c2.state



def test_three(cards_db):
    orig = [
        Card("foo"),
        Card("bar", owner="me"),
        Card("baz", owner="you", state="in prog"),
    ]

    for c in orig:
        cards_db.add_card(c)

    for c in orig:
        for c2 in cards_db.list_cards(state=c.state, owner=c.owner):
            assert c.state == c2.state and c.owner == c2.owner