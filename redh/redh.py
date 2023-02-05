#! /usr/bin/python3
import os
import re
import json
import click
import shutil
from pathlib import Path


RHAND_MEMORY = {'items': [], 'last_action': []}
ROOT_PATH = Path(os.getcwd(), __file__).parent


def write(data: dict) -> None:
    with open(Path(ROOT_PATH, 'redh_memory.json'), 'w') as redh_memory:
        json.dump(data, redh_memory)


def read() -> dict:
    with open(Path(ROOT_PATH, 'redh_memory.json'), 'r') as redh_memory:
        data = json.load(redh_memory)
        for item in data['items']:
            if not os.path.exists(item):
                data['items'].remove(item)
        write(data)
    return data


def display_contents(data: list, mode: str='open') -> None:
    try:
        if len(data) > 0:
            for index, item in enumerate(data):
                click.echo(
                    f"\033[94m{f'{index+1}' if index+1 < 10 else index+1}\033[0m - \033[92m{'f' if os.path.isfile(item) else 'd'}\033[0m - \033[93m{item}\033[0m")
        else:
            click.echo('\033[91mThe Hand is empty!\033[0m' if mode == 'open' else 'Nothing found!')

    except Exception: ...


def filtering(pattern: str, location, is_memory=False) -> list:
    try:
        if is_memory:
            filtered_items = [f"{location[index]}" for index, item in enumerate(location) if re.compile(pattern).search(item)]
        else:
            filtered_items = [f"{Path(os.getcwd(), location[index])}"
                              for index, item in enumerate(location) if re.compile(pattern).search(item)]
    except re.error as error:
        click.echo(error)
    else:
        return filtered_items


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
    else:
        if not Path(ROOT_PATH, 'redh_memory.json').exists():
            write(RHAND_MEMORY)


@main.command('open')
@click.option('-f', help='Filter display details.')
def open_hand(f):
    """
    The contents of the hand will be displayed.\n
    All contents have a numerical index that starts from one and will be selected with it.\n
    f: It means that the content is a file.\n
    d: It means that the content is a directory.\n
    """

    RHAND_MEMORY = read()

    if f:
        display_contents(filtering(f, RHAND_MEMORY['items'], is_memory=True))
    else:
        display_contents(RHAND_MEMORY['items'])


@main.command('scan')
@click.argument('filter', nargs=1)
def scan(filter):
    """Search and check the desired files and directories."""

    display_contents(filtering(filter, os.listdir(os.getcwd())), mode='scan')


@main.command('grab')
@click.argument('items', nargs=-1)
def grab(items):
    """The Redhand takes the files and directories you specified."""

    RHAND_MEMORY = read()
    for item in items:
        if item[0] == r"'" and item[-1] == r"'":
            filtered_items = filtering(item[1:-1], os.listdir(os.getcwd()))
            if len(filtered_items) > 0:
                for f_item in filtered_items:
                    if f_item not in RHAND_MEMORY['items']:
                        RHAND_MEMORY['items'].append(f_item)
                        click.echo(f"\033[93m'{f_item}' \033[92msuccessfully grabbed by hand!\033[0m")
                    else:
                        click.echo(f"\033[93m'{f_item}'\033[91m already in the hand!\033[0m")
            else:
                click.echo(f"\033[91mPattern \033[93m'{item}'\033[91m did not match anything!\033[0m")
        else:
            item_path = Path(os.getcwd(), Path(item).name)
            if item_path.exists():
                if str(item_path) not in RHAND_MEMORY['items']:
                    RHAND_MEMORY['items'].append(str(item_path))
                    click.echo(f"\033[93m'{str(item_path)}' \033[92msuccessfully grabbed by hand!\033[0m")
                else:
                    click.echo(f"\033[93m'{str(item_path)}'\033[91m already in the hand!\033[0m")
            else:
                click.echo(f"\033[93m'{str(item_path)}'\033[91m not found!\033[0m")

    write(RHAND_MEMORY)


@main.command('drop')
@click.option('-a', is_flag=True, help='All items will be released.')
@click.argument('indexes', nargs=-1, type=int)
def drop(a, indexes):
    """The Redhand leaves the files and directories it took in a specific place."""

    RHAND_MEMORY = read()

    if len(RHAND_MEMORY['items']) > 0:
        if a:
            for item in RHAND_MEMORY["items"]:
                item = Path(item)
                if item.is_file():
                    if Path(os.getcwd(), item.name).exists():
                        click.echo(f"\033[93m'{item.name}'\033[91m already exists!\033[0m")
                    else:
                        shutil.copyfile(item, item.name)
                        click.echo(f"\033[93m'{item}'\033[92m was copied successfully!\033[0m")
                else:
                    if Path(os.getcwd(), item.name).exists():
                        click.echo(f"\033[93m'{item.name}'\033[91m already exists!\033[0m")
                    else:
                        shutil.copytree(item, item.name)
                        click.echo(f"\033[93m'{item}'\033[92m was copied successfully!\033[0m")
        else:
            for index in indexes:
                if index == 0:
                    click.echo(f"\033[91mIndex out of range! >>> {index}\033[0m")
                else:
                    if index <= len(RHAND_MEMORY['items']):
                        item = Path(RHAND_MEMORY['items'][index-1])
                        if item.is_file():
                            if Path(os.getcwd(), item.name).exists():
                                click.echo(f"\033[93m'{item.name}'\033[91m already exists!\033[0m")
                            else:
                                shutil.copyfile(item, item.name)
                                click.echo(f"\033[93m'{item.name}'\033[92m was copied successfully!\033[0m")
                        else:
                            if Path(os.getcwd(), item.name).exists():
                                click.echo(f"\033[93m'{item.name}'\033[91m already exists!\033[0m")
                            else:
                                shutil.copytree(item, item.name)
                                click.echo(f"\033[93m'{item.name}'\033[92m was copied successfully!\033[0m")
                    else:
                        click.echo(f"\033[91mIndex out of range! >>> {index}\033[0m")
    else:
        click.echo("\033[91mThe Hand is empty!\033[0m")


@main.command('org')
@click.argument('args', nargs=2)
def organize(args):
    """Arranges and organizes the selected contents."""

    filtered_item = filtering(args[0], os.listdir(os.getcwd()))
    if len(filtered_item) > 0:
        dest_dir = Path(os.getcwd(), args[1])
        if not dest_dir.exists():
            dest_dir.mkdir()

        for item in filtered_item:
            file_path = Path(os.getcwd(), item)
            shutil.move(str(file_path), str(dest_dir))
            click.echo(f"\033[93m'{file_path}'\033[92m successfully moved to \033[93m'{dest_dir.name}'\033[92m directory!\033[0m")

    else:
        click.echo(f"\033[91mPattern \033[93m'{args[0]}'\033[91m did not match anything!\033[0m")


@main.command('throw')
@click.argument('indexes', nargs=-1, type=int)
def throw_away(indexes):
    """It discards the contents of the hand by their index."""

    RHAND_MEMORY, garbage = read(), []

    if len(RHAND_MEMORY['items']) > 0:
        for index in indexes:
            if index == 0:
                click.echo(f"\033[91mIndex out of range! >>> {index}\033[0m")
            else:
                if index <= len(RHAND_MEMORY['items']):
                    garbage.append(RHAND_MEMORY['items'][index-1])
                else:
                    click.echo(f"\033[91mIndex out of range! >>> {index}\033[0m")

        for item in garbage:
            if item in RHAND_MEMORY['items']:
                RHAND_MEMORY['items'].remove(item)
                click.echo(f"\033[93m'{item}' \033[92mwas successfully thrown away!\033[0m")

        write(RHAND_MEMORY)
    else:
        click.echo("\033[91mThe Hand is clean!\033[0m")


@main.command('wash')
def wash_hand():
    """All contents in the hand are completely erased."""

    RHAND_MEMORY = read()
    if len(RHAND_MEMORY['items']) > 0:
        RHAND_MEMORY['items'].clear()
        write(RHAND_MEMORY)
        click.echo("\033[92mThe Hand washed successfully!\033[0m")
    else:
        click.echo("\033[91mThe Hand is clean!\033[0m")


if __name__ == '__main__':
    main()