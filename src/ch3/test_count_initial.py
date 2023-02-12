from pathlib import Path
from tempfile import TemporaryDirectory
import cards


def test_empty():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        # print("db_path : ", db_path)
        db = cards.CardsDB(db_path)

        count = db.count()
        db.close()

        assert count == 0

if __name__ == '__main__':
    test_empty()