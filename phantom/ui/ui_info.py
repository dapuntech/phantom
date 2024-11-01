import util.constant as constant
import util.sys_info as sys_info
import subprocess
from prettytable import PrettyTable
from typing import Union

LINE = "-" * 25
package_info = sys_info.show_package_info()


def menu_banner() -> None:
    print(f"{constant.GREEN}{LINE}{constant.RESET}")
    print(f"{constant.RED}\tPhatom{constant.RESET}")
    print(f"{constant.GREEN}{LINE}{constant.RESET}")
    print(
        f"{constant.GREEN}version: {constant.RESET}{constant.BOLD}{constant.VERSION}{constant.RESET}"
    )

    menu_info()


def menu_info() -> None:
    print(f"{constant.NEWLINE}package info: {sys_info.show_package_info()}")
    print(f"{constant.BOLD}1. Available Tool{constant.RESET}")
    print(f"{constant.BOLD}2. Install Tool{constant.RESET}")


def installation(package_name: str) -> Union[list, None]:
    if package_info == "apt":
        command = ["sudo", "apt", "get", "install", package_name, "-y"]
    elif package_info == "pacman":
        command = ["sudo", "pacman", "-S", package_name, "--noconfirm"]
    elif package_info is None:
        print("Not Supported for non linux system")
    else:
        print("Unknown Linux Distro")

    try:
        package_install = subprocess.run(command, check=True)
        return package_install
    except subprocess.CalledProcessError:
        print("Error installing package")
        return None


def available_tool() -> None:
    list_of_tool = ["sqlmap", "metasploit"]
    table = PrettyTable()
    table.field_names = ["Available Tool"]
    for angka, data in enumerate(list_of_tool):
        table.add_row([f"{angka + 1} . {data}"])
    print(table)
    # print(f"{constant.NEWLINE}{constant.BOLD}Available Tool{constant.RESET}")
    # for number, data in enumerate(available_tool_hacking):
    #     print(f"{constant.BOLD}{number + 1}.{data}{constant.RESET}")


def install_tool() -> None:
    available_tool()
    input_data = input("enter your choice: ")
    if input_data == "1":
        print("installing sqlmap...")
        installation("sqlmap")


if __name__ == "__main__":
    print(installation())
