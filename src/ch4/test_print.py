
def test_normal():
    print("\n normal print")


def test_fail():
    print("\n print in failing test")
    assert False

def test_disabled(capsys):
    with capsys.disabled():
        print("\n capsys disabled print")

