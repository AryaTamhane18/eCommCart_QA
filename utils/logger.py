import logging
import sys


LOG_FORMAT = "%(asctime)s — %(levelname)s — %(message)s"
LOG_LEVEL = logging.DEBUG


def get_logger(name=__name__):
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(LOG_LEVEL)

        # Console Handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(LOG_LEVEL)
        console_formatter = logging.Formatter(LOG_FORMAT)
        console_handler.setFormatter(console_formatter)

        logger.addHandler(console_handler)

    return logger


log = get_logger("eCommLogger")
