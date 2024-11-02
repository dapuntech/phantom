import logging


def debug_log(name: str, log_file: str, show_console: bool = False) -> None:
    """
    setting buat debug logging

    Parameter:
        name(str): nama logger
        log_file(str): file logger yang di save
        level(logging.DEBUG): default DEBUG
    """
    if not isinstance(name, str) or not isinstance(log_file, str):
        print(f"error: name and log_file must be string, got {type(name)}")
    debug_mode = logging.DEBUG
    logger = logging.getLogger(name)
    logger.setLevel(debug_mode)

    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(debug_mode)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    if show_console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(debug_mode)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
