from os import mkdir, chdir
from json import dump, loads
from engine.actions import run
from shell import print_info, print_success

# Constants
CODE = 'outln Hello World!\n'

# Infos
infos = {
    'name': None,
    'version': None,
    'main': 'main.lyon',
    'description': None,
    'author': None
}


def start_msg() -> None:
    print_info('LyonManager: Running...')
    

def end_msg() -> None:
    print_info('LyonManager: Finished!')


def mkch_dir(name) -> None:
    mkdir(name)
    chdir(name)


def run_program(path, debug=True) -> None:
    try:
        with open(path + '\\lyon.json', 'r') as f:
            infos = loads(f.read())
    except Exception:
        show_info(f'Lyon: [red]Could not read "{path}"[/]')
    if debug:
        start_msg()
    chdir(path)
    chdir('src')
    run(infos['main'])
    if debug:
        end_msg()


def action_message(callback, message: str) -> None:
    print_success(f'{message}')
    callback()


def create_main_dir(name: str) -> None:
    try:
        mkch_dir(name)
    except Exception:
        show_info('Lyon: [red]Could not create the program.[/]')


def create_main_fn() -> None:
    mkch_dir('src')
    with open('main.lyon', 'w') as file:
        file.write(CODE)
    chdir('..')


def create_json() -> None:
    with open('lyon.json', 'w') as file:
        dump(infos, indent=4, fp=file)


def create_program(name: str) -> None:
    print_info(f'Lyon: [green]Creating program "{name}"[/]')
    infos['name'] = name
    infos['version'] = input('Version (default 1.0): ') or '1.0'
    infos['description'] = input(f'Description (default "{name}"): ') or name
    infos['author'] = input('Author (default "Unknown"): ') or 'Unknown'
    print_success(f'Lyon: Starting to create "{name}"')
    action_message(lambda: create_main_dir(name), 'Creating main directory')
    action_message(create_main_fn, 'Creating main function')
    action_message(create_json, 'Creating json file')
    print_success(f'Program "{name}" created!')


def show_info(title: str) -> None:
    print_success(title)
    print_info('Usage:')
    print_info('\t(lyon) --manage new <name>')
    print_info('\t(lyon) --manage run <program_path>')
    print_info('\t(lyon) --manage rundebug <program_path>')
    print_info('\t(lyon) --shell')
    exit(1)


def show_err(title: str) -> None:
    print_info(f'Lyon: [red]{title}[/]')
    print_info('Usage:')
    print_info('\t(lyon) new <name>')
    print_info('\t(lyon) run <program_path>')
    print_info('\t(lyon) rundebug <program_path>')
    exit(1)
