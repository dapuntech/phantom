import subprocess


def get_package_version(package_info: str | None, package_name: str) -> str:
    """
    Get the version of the package installed
    """

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
