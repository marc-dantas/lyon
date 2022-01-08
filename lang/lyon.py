# import engine
import shell


# TODO: Implementation of command interpretation
if __name__ == '__main__':
    shell.print_header(title='Lyon', subtitle='The command language')
    while True:
        cmd = shell.get()
        # FIXME: Temporary test
        print(cmd)