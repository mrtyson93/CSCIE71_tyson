import sys


def print_hello(name):
    print(f'Hello, {name}!')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hello(sys.argv[1])
