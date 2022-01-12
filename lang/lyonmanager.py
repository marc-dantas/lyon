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


def run(program_path):
    with open(program_path + '\\lyon.json', 'r') as f:
        infos = loads(f.read())
    msg_info(f'Lyon -> Running "{infos["name"]}" v{infos["version"]}')
    chdir(program_path)
    chdir('src')
    runfile(infos['main'])


def create_program(name, version):
    infos = {'name': name, 'version': version, 'main': 'main.lyon'}
    msg_success(f'Lyon: "{name}" v{version}')
    msg_info('Creating main directory')
    mkdir(name)
    chdir(name)
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
    if argv[1] == 'new':
        create_program(argv[2], argv[3])
        exit(1)
    elif argv[1] == 'run':
        run(argv[2])
        exit(1)


if __name__ == '__main__':
    main()
