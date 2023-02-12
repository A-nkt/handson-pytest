from pathlib import Path
from tempfile import TemporaryDirectory
import cards
import pytest


@pytest.fixture(scope='session')
def db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db_ = cards.CardsDB(db_path)
        yield db_
        db_.close()


@pytest.fixture(scope='function')
def cards_db(db):
    db.delete_all()
    return db


@pytest.fixture(scope='session')
def some_cards():
    return [
        cards.Card('write book', 'brian', 'done'),
        cards.Card('edit book', 'jun', 'done'),
        cards.Card('write 2nd edition', 'yuta', 'todo'),
        cards.Card('edit 2nd edition', 'kate', 'todo')
    ]


@pytest.fixture(scope='function')
def non_empty_db(cards_db, some_cards):
    for c in some_cards:
        cards_db.add_card(c)
    return cards_db