# Logging
import logging


def start_logger():
    logger = logging.getLogger("main-log")
    logger.setLevel(logging.DEBUG)
    log_format = logging.Formatter("%(levelname)8s | %(asctime)s | %(funcName)15s | %(message)s")

    # Build File Handler
    fh = logging.FileHandler(filename="./logs/game-container.log",)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(log_format)

    # Add Handlers to Logger
    logger.addHandler(fh)
    return logger


def get_logger():
    return logging.get_logger("main-log")
