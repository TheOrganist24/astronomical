"""Utility module for initalising logging."""

from loguru import logger
import os
import sys


def setup_logging():
    """Initialise logging and return logger."""
    log_levels = [
        "DEBUG",  # only for diagnosis
        "INFO",  # things are working as expected
        "WARNING",  # nothing is broken, just something unexpected happened
        "ERROR",  # something has broken
        "CRITICAL"  # everything is on fire
    ]
    logger.remove()
    logger.add("astronomical.log", level="INFO")
    log_level = os.getenv("LOG_LEVEL")
    if not log_level:
        logger.add(sys.stdout, level="ERROR")
    elif log_level in (log_levels):
        logger.add(sys.stdout, level=log_level)
    else:
        logger.add(sys.stdout, level="DEBUG")
        logger.warning(f"LOGGING: Mistyped environment variable;\n"
                       f"\ttry one of {log_levels}\n"
                       f"\teg. `export LOG_LEVEL=DEBUG`.\n"
                       f"\tLog level will be set to \"DEBUG\".")


def log_calculations(func):
    """Decorate to log calculations."""
    def wrap(*args, **kwargs):
        logger.debug(f"Calculation \"{func.__name__}\" invoked.")
        return func(*args, **kwargs)
    return wrap
