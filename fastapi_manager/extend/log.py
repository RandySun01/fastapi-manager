# sys
import logging

# 3p
from fastapi import FastAPI

DefaultLogFormatter = '%(asctime)s | %(levelname)s | %(message)s'
DefaultLogLevel = logging.INFO


def logger_extend(app: FastAPI):
    """ Simple configuration of logs
    """
    # setting: Configuration variables
    setting = app.state.setting
    ignore_loggers = getattr(setting, 'IgnoreLogger', [])
    log_level = getattr(setting, 'LogLevel', DefaultLogLevel)
    log_formatter = getattr(setting, 'LogFormatter', DefaultLogFormatter)

    # Filtering the logs of other packets
    for ignore_logger in ignore_loggers:
        ignore_log = logging.getLogger(ignore_logger)
        ignore_log.disabled = True

    # Log configuration
    logger = logging.getLogger()
    logger.setLevel(log_level)
    ch = logging.StreamHandler()
    formatter = logging.Formatter(log_formatter)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
