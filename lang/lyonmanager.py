from sys import argv
from os import mkdir, chdir
from time import sleep
from json import dump, loads
from engine.actions import runfile
from shell import print_info, print_success


def msg_info(title):
    print_info(f'{title}...')


def msg_success(title):
    print_success(f'{title}')


def run(program_path, debug=True):
    with open(program_path + '\\lyon.json', 'r') as f:
        infos = loads(f.read())
    if debug:
        msg_info(f'LyonManager: Running "{infos["name"]}" v{infos["version"]}')
    chdir(program_path)
    chdir('src')
    runfile(infos['main'])
    if debug:
        msg_info(f'LyonManager: Finished "{infos["name"]}" v{infos["version"]}')


def create_program(name, version, description, author):
    infos = {
        'name': name,
        'version': version,
        'main': 'main.lyon',
        'description': description,
        'author': author
    }
    msg_success(f'Lyon: "{name}" v{version}')
    msg_info('Creating main directory')
    try:
        mkdir(name)
        chdir(name)
    except FileExistsError:
        show_info(f'Lyon: [red]Directory "{name}" already exists[/]')
        exit(1)
    msg_info('Creating src directory')
    mkdir('src')
    chdir('src')
    msg_info('Creating main function')
    with open('main.lyon', 'w') as file:
        file.write('outln Hello World!\n')
    chdir('..')
    msg_info('Creating lyon.json')
    with open('lyon.json', 'w') as file:
        dump(infos, indent=4, fp=file)
    msg_success(f'Program "{name}" v{version} created!')


def main():
    if len(argv) > 1:
        if argv[1] == 'new' and len(argv) > 5:
            create_program(argv[2], argv[3], argv[4], argv[5])
        elif argv[1] == 'rundebug':
            run(argv[2])
        elif argv[1] == 'run':
            run(argv[2], debug=False)
        else:
            show_info('Lyon Manager: [red]Invalid command or argument syntax[/]')
    else:
        show_info('Lyon Manager')
    exit(1)


def show_info(title):
    print_success(title)
    print_info('Usage:')
    print_info('\tlyon.py new <name> <version> <description> <author>')
    print_info('\tlyon.py run <program_path>')
    print_info('\tlyon.py rundebug <program_path>')


if __name__ == '__main__':
    main()
