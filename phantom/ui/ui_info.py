import util.constant as constant
import util.package as sys_info
import util.package as package_version
import subprocess
import json
from prettytable import PrettyTable
from typing import Union
import time
import threading
import requests
import os


package_info = sys_info.show_package_info()
done = False


# do not change this function unless you are maintainer
def menu_banner() -> None:
    print(f"""{constant.BOLD}{constant.RED}
██████╗░██╗░░██╗░█████╗░███╗░░██╗████████╗░█████╗░███╗░░░███╗
██╔══██╗██║░░██║██╔══██╗████╗░██║╚══██╔══╝██╔══██╗████╗░████║
██████╔╝███████║███████║██╔██╗██║░░░██║░░░██║░░██║██╔████╔██║
██╔═══╝░██╔══██║██╔══██║██║╚████║░░░██║░░░██║░░██║██║╚██╔╝██║
██║░░░░░██║░░██║██║░░██║██║░╚███║░░░██║░░░╚█████╔╝██║░╚═╝░██║
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝
{constant.NEWLINE}{constant.RESET}
""")
    print(
        f"{constant.message_color('green', 'version:')}{constant.BOLD}{constant.VERSION}"
    )
    print(
        f"{constant.message_color('green', 'package version:')} {sys_info.show_package_info()}{constant.NEWLINE}"
    )

    menu_info()


def menu_info() -> None:
    """
    Information about menu information, currently showing
        - available tool: list of tool available
        - install tool: install tool
    """
    print(f"{constant.BOLD}1. Available Tool{constant.RESET}")
    print(f"{constant.BOLD}2. Install Tool{constant.RESET}")


# Spinner function to display loading
def spinner(package_name: str) -> None:
    """
    Spinner function to display loading

    Parameter:
        package_name(str): package name to showing on package name
    """
    if not isinstance(package_name, str):
        print(
            f"{constant.message_color('red', 'error:')} package must be string, not {type(package_name)}"
        )
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


def run_install(command: list[str], package_name: str) -> None:
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
            f"\r{constant.message_color('green', 'Successfully installed')} {package_name} (version: {version})"
        )
    except subprocess.CalledProcessError:
        done = True
        spinner_thread.join()
        print(constant.message_color("red", "\rError installing package"))


def install_from_repository(package_name: str) -> Union[list, None]:
    """
    function to install package from its repository

    Parameter:
        package_name(str): package to install

    return:
        - list: list of package installed
        - None: if package is not supported
    """

    spinner_thread = threading.Thread(target=spinner, args=(package_name,))
    try:
        global done

        # Load the list of package repository
        with open("phantom/ui/list_package_repo.txt", "r") as file:
            loaded_repo = json.load(file)
        list_repo = loaded_repo

        # Run sudo before installing to make sure user has permission to install
        subprocess.run(
            ["sudo", f"{package_info}"],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        spinner_thread.start()

        # Downloading the script from the repository
        response = requests.get(list_repo[package_name])

        # Check if the response status code is 200
        if response.status_code == 200:
            # Save the script to a file named {package_name}
            with open(package_name, "w") as file:
                file.write(response.text)

            # Make the script executable
            os.chmod(package_name, 0o755)

            done = True
            spinner_thread.join()

            # Installing {package_name}
            print("\n")
            subprocess.run(
                [f"./{package_name}"],
                shell=True,
                check=True,
            )
        else:
            # If the response status code is not 200, print an error message
            done = True
            spinner_thread.join()
            print(f"Failed to download script: HTTP status code {response.status_code}")
    except Exception as e:
        # Catch any exception
        done = False
        spinner_thread.join()
        print(f"failed to install {package_name}: {e}")
    finally:
        # Clean up installed script
        print("cleaning up...")
        done = True
        spinner_thread.join()
        if os.path.exists(package_name):
            os.remove(package_name)


def install_package(package_name: str) -> Union[list, None]:
    """
    function to install package

    Parameter:
        package_name(str): package to install

    return:
        - list: list of package installed
        - None: if package is not supported
    """
    if not isinstance(package_name, str):
        print(
            f"{constant.message_color('red', 'error:')}package must be string, not {type(package_name)}"
        )
    if package_info == "apt":
        command = ["sudo", "apt-get", "install", package_name, "-y"]
        run_install(command, package_name)
    elif package_info == "pacman":
        command = ["sudo", "pacman", "-S", package_name, "--noconfirm"]
        run_install(command, package_name)
    elif package_info is None:
        print("Not Supported for non linux system")
    else:
        print("Unknown Linux Distro")


def available_tool() -> None:
    """
    function to show available tool
    """
    with open("phantom/ui/list_of_tool.txt", "r") as file:
        loaded_tool_list = json.load(file)
    list_of_tool = loaded_tool_list

    table = PrettyTable()
    table.field_names = ["No", "Available Tool", "Description"]
    for angka, data in enumerate(list_of_tool):
        table.add_row([f"{angka + 1}", data, f"{list_of_tool[data]}"])
    print(table)


def install_tool() -> None:
    """
    function to install available tools
    """
    available_tool()
    input_data = int(input("enter your choice for installation: "))
    if not isinstance(input_data, int):
        print(constant.message_color("red", "input data must be int"))
    match input_data:
        case 1:
            install_package("sqlmap")
        case 2:
            install_from_repository("metasploit")
        case 3:
            install_package("nmap")
        case 4:
            install_package("aircrack-ng")
        case 5:
            install_package("airflood")
        case 6:
            install_package("hping")
        case 7:
            install_package("bettercap")
        case _:
            print(
                f"{constant.message_color('red', 'invalid choice')}{constant.NEWLINE}{constant.message_color('yellow', 'TODO:')} implemented{constant.NEWLINE}"
            )
