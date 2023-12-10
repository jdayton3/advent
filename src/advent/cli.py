import click
from importlib import import_module
from importlib.resources import files

@click.command()
@click.argument("exercise", type=str)
def cli(exercise: str) -> None:
    """EXERCISE: {day}-{part}, e.g., 06-2 for day 6, part 2"""
    day, part = exercise.split("-")
    day = day.zfill(2)
    module = import_module(f"advent.day{day}", "advent")
    fn = getattr(module, f"part{part}")
    infile = files("advent.inputs").joinpath(f"{day}-{part}.txt")
    result = fn(infile.read_text())
    click.echo(result)

if __name__ == "__main__":
    cli()
