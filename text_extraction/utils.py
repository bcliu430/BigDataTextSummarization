import logging
from dynaconf import settings

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
FORMATTER = logging.Formatter(LOG_FORMAT, datefmt="%Y-%m-%d %H:%M:%S")
LEVELS = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "error": logging.ERROR,
    "warning": logging.WARNING
}


def get_level(level):
    return LEVELS[level]


def create_handler(handler_type):
    if handler_type == "stream":
        handler = logging.StreamHandler()
        handler.setFormatter(FORMATTER)
        handler.setLevel(get_level(settings.LOG_LEVEL))
    elif handler_type == "file":
        # Set file handler with level specified
        filename = settings.LOG_FILE
        handler = logging.FileHandler(filename)
        handler.setFormatter(FORMATTER)
        handler.setLevel(get_level(settings.LOG_LEVEL))
    else:
        handler = None
    return handler


def create_error_handler():
    # Set file handler with only error messages
    filename = settings.ERROR_FILE
    handler = logging.FileHandler(filename)
    handler.setFormatter(FORMATTER)
    handler.setLevel(logging.ERROR)
    return handler


def setup_logger():
    logger = logging.getLogger("GROBID Parser")

    # Set up handlers
    handlers = settings.LOG_HANDLERS
    for handler_type in handlers:
        handler = create_handler(handler_type)
        if handler is not None:
            logger.addHandler(handler)
        if handler_type == "file":
            logger.addHandler(create_error_handler())

    logger.setLevel(get_level(settings.LOG_LEVEL))

    return logger


logger = setup_logger()
