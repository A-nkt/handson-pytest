from pathlib import Path
from tempfile import TemporaryDirectory
import cards
import pytest

from test_tmp import test_tmp_path_factory

@pytest.fixture(scope="session")
def db():
    db_path = test_tmp_path_factory(db_path)
    db_ = cards.CardsDB()
    yield db_
    db_.close()