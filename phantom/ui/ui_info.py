import util.constant as constant
import util.sys_info as sys_info
import util.package_version as package_version
import subprocess
from prettytable import PrettyTable
from typing import Union
import time
import threading

LINE = "-" * 25
package_info = sys_info.show_package_info()
done = False


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


# Spinner function to display loading
def spinner(package_name: str):
    # Define the spinner characters
    spinner_chars = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]

    # Initialize the index
    idx = 0

    # Loop until the done flag is set to True
    while not done:
        print(
            f"\rInstalling {package_name}... {spinner_chars[idx]}{constant.RESET}",
            end="",
            flush=True,
        )
        idx = (idx + 1) % len(spinner_chars)
        time.sleep(0.1)


def install(command: list[str], package_name: str) -> None:
    global done

    # Create a thread to run the loading spinner
    spinner_thread = threading.Thread(target=spinner, args=(package_name,))
    try:
        done = False

        # Run sudo before installing to make sure user has permission to install
        subprocess.run(
            ["sudo", f"{package_info}"],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        # Start loading spinner thread
        spinner_thread.start()

        # Run the installation command
        subprocess.run(
            command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )

        # Wait for the spinner thread to finish
        done = True
        spinner_thread.join()

        # Wait for the spinner thread to finish
        version = package_version.get_package_version(package_info, package_name)

        print(
            f"\r{constant.GREEN}Successfully installed {package_name} (version: {version}){constant.RESET}"
        )
    except subprocess.CalledProcessError:
        done = True
        spinner_thread.join()
        print("\rError installing package")


def installation(package_name: str) -> Union[list, None]:
    if package_info == "apt":
        command = ["sudo", "apt-get", "install", package_name, "-y"]
        install(command, package_name)
    elif package_info == "pacman":
        command = ["sudo", "pacman", "-S", package_name, "--noconfirm"]
        install(command, package_name)
    elif package_info is None:
        print("Not Supported for non linux system")
    else:
        print("Unknown Linux Distro")


def available_tool() -> None:
    list_of_tool = {
        "sqlmap": "Automates SQL injection testing and exploitation.",
        "metasploit": "Framework for developing and executing exploits.",
        "nmap": "Comprehensive tool for network scanning and discovery.",
    }

    table = PrettyTable()
    table.field_names = ["No", "Available Tool", "Description"]
    for angka, data in enumerate(list_of_tool):
        table.add_row([f"{angka + 1}", data, f"{list_of_tool[data]}"])
    print(table)
    # print(f"{constant.NEWLINE}{constant.BOLD}Available Tool{constant.RESET}")
    # for number, data in enumerate(available_tool_hacking):
    #     print(f"{constant.BOLD}{number + 1}.{data}{constant.RESET}")


def install_tool() -> None:
    available_tool()
    input_data = input("enter your choice: ")
    if input_data == "1":
        installation("sqlmap")
    elif input_data == "3":
        installation("nmap")


if __name__ == "__main__":
    print(installation())
