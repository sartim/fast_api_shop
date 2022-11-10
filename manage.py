import os
import click

from dotenv import load_dotenv

load_dotenv()


@click.group()
def main():
    """This is a management script for the application."""


@main.command("create_migration", short_help="Create new migration version.")
@click.option("--message", help="Migration message")
def create_migration(**kwargs):
    os.system(
        'alembic revision --autogenerate -m "{}"'.format(kwargs.get("message")))


@main.command("migrate", short_help="Updates database revision.")
def create_migration():
    os.system("alembic upgrade head")


@main.command("run_server", short_help="Run development server.")
def run_server():
    os.system("uvicorn main:app --reload")


cli = click.CommandCollection(sources=[main])


if __name__ == "__main__":
    cli()
