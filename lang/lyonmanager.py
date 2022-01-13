from sys import argv
from os import mkdir, chdir
from time import sleep
from json import dump, loads
from engine.actions import run
from shell import print_info, print_success


msg_info = print_info
msg_success = print_success


def runp(program_path, debug=True):
    try:
        with open(program_path + '\\lyon.json', 'r') as f:
            infos = loads(f.read())
    except FileNotFoundError:
        show_info(f'Lyon Manager: [red]Program "{program_path}" not found[/]')
        exit(1)
    except Exception:
        show_info(f'Lyon Manager: [red]Could not read "{program_path}"[/]')
    if debug:
        msg_info(f'LyonManager: Running "{infos["name"]}" v{infos["version"]}')
    chdir(program_path)
    chdir('src')
    run(infos['main'])
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
    except Exception:
        show_info('Lyon: [red]Could not create the program.[/]')
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
        elif argv[1] == 'rundebug' and len(argv) > 2:
            runp(argv[2])
        elif argv[1] == 'run' and len(argv) > 2:
            runp(argv[2], debug=False)
        else:
            show_info('Lyon Manager: [red]Invalid command or argument syntax[/]')
    else:
        show_info('Lyon Manager')
    exit(1)


def show_info(title):
    print_success(title)
    print_info('Usage:')
    print_info('\t(lyonmanager) new <name> <version> <description> <author>')
    print_info('\t(lyonmanager) run <program_path>')
    print_info('\t(lyonmanager) rundebug <program_path>')


if __name__ == '__main__':
    main()
