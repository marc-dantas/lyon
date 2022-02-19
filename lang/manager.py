from os import mkdir, chdir
from json import dump, loads
from engine.actions import cmd_call
from shell import print_info, print_success

# Constants
CODE = 'outln "Hello World!"\n'

# Infos
infos = {
    'name': None,
    'version': None,
    'main': 'src/main.lyon',
    'description': None,
    'author': None
}


def start_msg() -> None:
    print_info('Lyon: Running...')
    

def end_msg() -> None:
    print_info('Lyon: Finished!')


def mkch_dir(name) -> None:
    mkdir(name)
    chdir(name)


def run_program(path, debug=True) -> None:
    try:
        with open(f'{path}\\lyon.json', 'r') as f:
            infos = loads(f.read())
        if debug:
            start_msg()
        chdir(path)
        cmd_call(infos['main'])
        if debug:
            end_msg()
    except Exception:
        show_info(f'Lyon: [red]Could not read "{path}"[/]')


def action_message(callback, message: str) -> None:
    print_success(f'{message}')
    callback()


def create_main_dir(name: str) -> None:
    try:
        mkch_dir(name)
    except Exception:
        show_info('Lyon: [red]Could not create the program.[/]')


def create_main_fn(default_code=True) -> None:
    mkch_dir('src')
    with open('main.lyon', 'w') as file:
        if default_code:
            file.write(CODE)
    chdir('..')


def create_json() -> None:
    with open('lyon.json', 'w') as file:
        dump(infos, indent=4, fp=file)


def create_program(name: str) -> None:
    print_info(f'Lyon: [green]Creating program "{name}"[/]')
    infos['name'] = name
    infos['version'] = input('Version (default 1.0): ').strip() or '1.0'
    infos['description'] = input(f'Description (default "{name}"): ').strip() or name
    infos['author'] = input('Author (default "Unknown"): ').strip() or 'Unknown'
    default_code = input('Start with default code? (Y/n) ').strip().lower() or 'y'
    print_success(f'Lyon: Starting to create "{name}"')
    action_message(lambda: create_main_dir(name), 'Creating main directory')
    action_message(
        lambda: create_main_fn(1 if default_code == 'y' else 0),
        'Creating main function')
    action_message(create_json, 'Creating json file')
    print_success(f'Program "{name}" created!')


def show_info(title: str) -> None:
    print_success(title)
    print_info('Usage:')
    print_info('\t(lyon) --manage | -m new <name>')
    print_info('\t(lyon) --manage | -m run <program_path>')
    print_info('\t(lyon) --manage | -m rundebug <program_path>')
    print_info('\t(lyon) --shell | -s')
    print_info('\t(lyon) --version | -v')
    print_info('\t(lyon) --command | -c <command>')
    exit(1)
