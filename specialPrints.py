import time
from termcolor import colored


def cyan_later_print(object: any):
    time.sleep(0.4)
    print(colored(object, "light_cyan"))


def cyan_input(object: any):
    x = input(colored(object, "light_cyan"))
    return x


def cyan_now_print(object: any):
    print(colored(object, "light_cyan"))


def error_message(object: any):
    print(colored(object, "light_red"))


if __name__ == '__main__':
    cyan_later_print("Hello, world!")
    cyan_later_print("Hello, world!")
    cyan_later_print("Hello, world!")
    cyan_later_print("Hello, world!")
    cyan_input(">")
