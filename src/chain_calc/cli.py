# -*- coding: utf-8 -*-
"""Console script for chain_calc."""
import logging
import sys

import click

from . import __version__
from .utils import count_to_log_level


def print_help(ctx, param, value):
    if value:
        click.echo(ctx.get_help())
        if param is None:
            ctx.exit(1)
        ctx.exit(0)


def print_version(ctx, param, value):
    if value:
        click.echo(__version__)
        ctx.exit(0)


@click.command()
@click.argument("number", metavar="NUMBER", nargs=-1)
@click.option(
    "--help",
    "-h",
    help="Show this message and exit.",
    is_flag=True,
    expose_value=False,
    callback=print_help,
)
@click.option(
    "--version",
    "-V",
    help="Print version and exit.",
    is_flag=True,
    expose_value=False,
    callback=print_version,
)
@click.option(
    "--dry-run",
    "-n",
    flag_value="dry_run",
    default=False,
    help="Perform a trial run with no changes made.",
)
@click.option(
    "--verbose",
    "-v",
    count=True,
    help="Increase verbosity (specify multiple times for more).",
)
@click.pass_context
def main(ctx, number, dry_run, verbose):
    """Console script for test_cli_project."""

    if dry_run:
        click.echo("This is merely a dry run")
        return 0

    if len(number) == 1:
        number = next(iter(number))
        click.echo(number)
    else:
        if len(number) > 1:
            click.echo(f"Error: expecting 1 number, got {len(number)}")
        print_help(ctx, None, True)

    logging.basicConfig(level=count_to_log_level(verbose))
    logging.warning("This is a warning.")
    logging.info("This is an info message.")
    logging.debug("This is a debug message.")

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
