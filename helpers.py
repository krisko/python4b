from colorama import Fore


def display(msg, isWarn=False):
    if isWarn:
        print(Fore.RED + 'WARNING!! ' + msg + Fore.RESET)
    else:
        print(Fore.BLUE + msg + Fore.RESET)


def error(msg, isErr=False):
    if isErr:
        print('ERROR!! ' + msg)
    else:
        print(msg)
