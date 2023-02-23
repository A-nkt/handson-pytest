from subprocess import run
import sums

def test_sums():
    result = run(['python', 'sums.py', 'data.txt'], capture_output=True, text=True)
    output = result.stdout
    assert output == '200.00\n'

def test_sums_2():
    result = run(['python', 'sums.py', 'data.txt', 'data2.txt'], capture_output=True, text=True)
    output = result.stdout
    assert output == '500.00\n'