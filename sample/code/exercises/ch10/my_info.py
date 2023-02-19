from pathlib import Path
from unittest import mock

def home_dir():
    return str(Path.home())


def test_home_dir():
    with mock.patch('home_dir') as f:
        print(f)
        # assert f.return_value == "Users/fake_user"

if __name__ == "__main__":
    print(home_dir())
