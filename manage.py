import os
import click

from dotenv import load_dotenv


load_dotenv()


@click.group()
def main():
    """This is a management script for the application."""


@main.command("runserver", short_help="Run development server.")
def runserver():
    os.system("uvicorn main:app --reload")


cli = click.CommandCollection(sources=[main])


if __name__ == "__main__":
    cli()
