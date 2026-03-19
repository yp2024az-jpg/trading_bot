import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logger(name='trading_bot', log_file='logs/bot.log', level=logging.INFO):
    log_dir = Path(log_file).parent
    log_dir.mkdir(exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh = RotatingFileHandler(log_file, maxBytes=10**6, backupCount=5)
    fh.setLevel(level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

