import hello_world


def test_hello_v1():
    hello_world.hello()
    with open('hello.txt', 'r') as f:
        data = f.read()
    assert data == 'Hello World!\n'


def test_hello_v2(tmp_path):
    file = tmp_path / 'file.txt'
    file.write_text('Hello World!\n')
    assert file.read_text() == 'Hello World!\n'


