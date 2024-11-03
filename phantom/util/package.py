import subprocess
import platform
import util.debug_phantom as debug
from typing import Union


def get_package_version(package_info: Union[str, None], package_name: str) -> str:
    """
    Get the version of the package installed

    Parameters:
        package_info (str): The package manager used (apt or pacman)
        package_name (str): The name of the package
    """

    if not isinstance(package_info, str) and not isinstance(package_name, str):
        print(
            f"error: package_info and package_name must be string, got {type(package_info)}"
        )

    if package_info == "apt":
        # Use apt-cache policy to get the installed version of the package
        command = ["apt-cache", "policy", package_name]

        # Run the command and capture the output
        output = subprocess.run(command, capture_output=True, text=True)
        for line in output.stdout.splitlines():
            if "Installed:" in line:
                return line.split(": ")[1].strip()
    elif package_info == "pacman":
        # Use pacman -Qi to get the installed version of the package
        command = ["pacman", "-Qi", package_name]

        # Run the command and capture the output
        output = subprocess.run(command, capture_output=True, text=True)
        for line in output.stdout.splitlines():
            if "Version" in line:
                return line.split(": ")[1].strip()

    return "unknown"


def show_package_info() -> Union[str, None]:
    """
    get package manager info on specific linux distro

    return:
        - str: package manager info
        - None: if package is not supported
    """
    logger = debug.debug_log("show_package_info", "os_package.log")
    os_info = platform.system()
    if os_info == "Linux":
        try:
            with open("/etc/os-release", "r") as f:
                linux_info = f.read().lower()
            if "debian" in linux_info or "ubuntu" in linux_info:
                logger.info("debian or Ubuntu Based Linux")
                return "apt"
            elif "arch" in linux_info:
                logger.debug("Arch based Linux")
                return "pacman"
            else:
                logger.warning("Unknown Linux Distro")
                return None
        except FileNotFoundError:
            logger.error("File Not Found")
            return None
    else:
        logger.error("Not Supported for non linux system")
        return None
