
def print_header(title, subtitle=None) -> None:
    print('=' * 40)
    print(title.center(40))
    if subtitle:
        print(subtitle.center(40))
    print('=' * 40)


def get() -> str:
    return input('> ')
