import click
import shutil
import sqlite3
from pathlib import Path


@click.group(invoke_without_command=True)
@click.option('--version', is_flag=True, help='Version of Redhand.')
def main(version):
    """
    Redhand is a command line tool for managing files and directories.\n
    To access the help of each command, use the --help option after writing the command.\n
    Github repo: https://github.com/mimseyedi/redh\n
    """
    if version:
        click.echo('1.0.0')


@main.command('open')
@click.option('-f', help='Filter display details.')
@click.option('-h', is_flag=True, help='Show head of contents.')
@click.option('-t', is_flag=True, help='Show tail of contents.')
def open_hand(f, h, t):
    """
    The contents of the hand will be displayed.\n
    All contents have a numerical index that starts from one and will be selected with it.\n
    f: It means that the content is a file.\n
    d: It means that the content is a directory.\n
    """
    pass


@main.command('scan')
@click.argument('filter', nargs=1)
def scan(filter):
    """Search and check the desired files and directories."""
    pass


@main.command('grab')
@click.option('-c', is_flag=True, help='A copy is taken of the desired item.')
@click.argument('items', nargs=-1)
def grab(c):
    """The Redhand takes the files and directories you specified."""
    pass


@main.command('drop')
@click.option('-x', is_flag=True, help='The contents will be cut.')
@click.argument('items', nargs=-1)
def drop(x):
    """The red hand leaves the files and directories it took in a specific place."""
    pass


@main.command('org')
@click.argument('filter', nargs=-1)
def organize(filter):
    """Arranges and organizes the selected contents."""
    pass


if __name__ == '__main__':
    main()