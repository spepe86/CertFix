import logging
from logging.handlers import RotatingFileHandler


def setup_logging(log_file='ldcertfix.log'):
    logger = logging.getLogger('ldcertfix')
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(log_file, maxBytes=1_000_000, backupCount=3, encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
