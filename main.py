from colorama import Fore, Style

def print_colored_text():
    print(Fore.RED + "This text is red!")
    print(Fore.GREEN + "This text is green!")
    print(Fore.BLUE + "This text is blue!")
    print(Style.RESET_ALL + "This text is back to normal.")

if __name__ == "__main__":
    print_colored_text()