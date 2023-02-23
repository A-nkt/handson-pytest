import typer
from typing import List, Optional


app = typer.Typer()

@app.command()
def main(file):
    sum = 0.0

    for fi in file:
        with open(fi, "r") as f:
            for line in f:
                number = float(line)
                sum += number
    print(f"{sum:.2f}")


if __name__ == '__main__':
    app()
