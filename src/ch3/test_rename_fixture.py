import pytest


@pytest.fixture(name='utlimate_answer')
def ultimate_answer_fixture():
    return 42


def test_everything(utlimate_answer):
    assert utlimate_answer == 42

