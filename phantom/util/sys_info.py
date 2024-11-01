import platform
import util.debug_phantom as debug
from typing import Union


def show_package_info() -> Union[str, None]:
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
