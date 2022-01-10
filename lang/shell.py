
def print_header(title, subtitle=None) -> None:
    print('=' * 40)
    print(title.center(40))
    if subtitle:
        print(subtitle.center(40))
    print('=' * 40)


def print_hint(hint: str) -> None:
    print(f"-> {hint}")


def get() -> str:
    return input('\n>>> ')
