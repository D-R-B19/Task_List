import logging


def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(pastime)s - %(name)s - %(levelness)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
