from subprocess import run
import sums
from typer.testing import CliRunner

runner = CliRunner()

def test_sums():
    result = runner.invoke(sums.app, ['data.txt'])
    assert result.stdout == '200.00\n'

def test_sums_2():
    result = run(['python', 'sums.py', 'data.txt', 'data2.txt'], capture_output=True, text=True)
    output = result.stdout
    assert output == '500.00\n'