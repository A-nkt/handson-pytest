import pytest

@pytest.fixture(name='list_value', scope='module')
def sample_data():
    """
    hello this is sample fixture
    """
    print('--start--')
    yield [1, 2, 3]
    print('--finish--')


def test_sample_data(list_value):
    assert list_value == [1, 2, 3]



def test_sample_data2(list_value):
    assert [3, 1, 2] != list_value