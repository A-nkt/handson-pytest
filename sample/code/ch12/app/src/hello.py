import typer
from typing import Optional


def full_output(name: str):
    return f"Hello, {name}!"


app = typer.Typer()


@app.command()
def main(name: Optional[str] = typer.Argument("World")):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    app()
