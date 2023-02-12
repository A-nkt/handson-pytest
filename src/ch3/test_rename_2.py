import pytest
from somewhere import  app

@pytest.fixture(scope='session', name=app)
def _app():
    yield app()

def test_that_uses_app():
    assert app.some_property == 'something'