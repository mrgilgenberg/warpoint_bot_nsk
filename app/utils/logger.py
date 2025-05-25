import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
import sys

logger = logging.getLogger('Bots')


def setup_logger(path, name, level):
    if level not in ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'):
        raise Exception(f"Incorrect level: {level}")

    log_level = getattr(logging, level)

    # Форматтер для всех обработчиков
    strfmt = '%(asctime)s [%(levelname)s] [%(funcName)s] > %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(fmt=strfmt, datefmt=datefmt)

    # Файловый обработчик
    log_handler = TimedRotatingFileHandler(
        filename=Path(path, name),
        when='midnight',
        interval=1,
        backupCount=7,
        encoding='utf-8'
    )
    log_handler.setFormatter(formatter)

    # Консольный обработчик
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # Настройка вашего логгера
    bot_logger = logging.getLogger('Bots')
    bot_logger.setLevel(log_level)
    bot_logger.addHandler(log_handler)
    bot_logger.addHandler(console_handler)

    # Настройка логгера aiogram
    aiogram_logger = logging.getLogger('aiogram')
    aiogram_logger.setLevel(log_level)
    aiogram_logger.addHandler(log_handler)
    aiogram_logger.addHandler(console_handler)