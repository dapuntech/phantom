from colorama import Fore, Style

VERSION_MAJOR: str = "1"
VERSION_MINOR: str = "0"
VERSION_PATCH: str = "0"
VERSION: str = VERSION_MAJOR + "." + VERSION_MINOR + "." + VERSION_PATCH

RED: str = Fore.RED
GREEN: str = Fore.GREEN
YELLOW: str = Fore.YELLOW
BLUE: str = Fore.BLUE
MAGENTA: str = Fore.MAGENTA
CYAN: str = Fore.CYAN
WHITE: str = Fore.WHITE
BOLD: str = Style.BRIGHT
RESET: str = Style.RESET_ALL
NEWLINE: str = "\n"


def message_color(color: str, message: str) -> str:
    if not isinstance(color, str) or not isinstance(message, str):
        print(f"color: {type(color)}" f"message: {type(message)}")
    if color not in ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]:
        print(
            f"error: color must be red, green, yellow, blue, magenta, cyan, white, got {color}"
        )
    else:
        if color == "green":
            msg = f"{GREEN}{message}{RESET}"
        elif color == "red":
            msg = f"{RED}{message}{RESET}"
        elif color == "yellow":
            msg = f"{YELLOW}{message}{RESET}"
        elif color == "blue":
            msg = f"{BLUE}{message}{RESET}"
        elif color == "magenta":
            msg = f"{MAGENTA}{message}{RESET}"
        elif color == "cyan":
            msg = f"{CYAN}{message}{RESET}"
        elif color == "white":
            msg = f"{WHITE}{message}{RESET}"
    return msg


if __name__ == "__main__":
    print(f"{GREEN} test {RESET}")
