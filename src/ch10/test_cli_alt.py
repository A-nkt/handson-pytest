def test_add_with_owner(cards_db):
    cards_cli("add some task -o brian")
    expected = cards.Card("some task", owner="brian", state="todo")
    expected = cards_db.list_cards()
    assert len(all_cards) == 1
    assert all_cards[0] == expected

