
def print_header(title, subtitle=None) -> None:
    print(f" {title} ".center(80, '-'))
    if subtitle:
        print(f" {subtitle} ".center(80, '-'))


def print_hint(hint: str) -> None:
    print(f"\t-> {hint}")


def get() -> str:
    return input('>>> ')
