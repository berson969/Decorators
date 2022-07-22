import logging
from logging import Logger
from functools import wraps


def decor_logging(path_log):

    def _logging(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(__name__)
            logger.setLevel(logging.INFO)
            fileHandler = logging.FileHandler(path_log)
            fileHandler.setFormatter(logging.Formatter(fmt='%(asctime)s: %(message)s'))
            logger.addHandler(fileHandler)
            result = func(*args, **kwargs)
            title = str(args[0]).strip("<span>")[:90]
            msg = f'FuncName: {func.__name__}: Result {result} =>> Title {title}'
            logger.info(msg)
            # fileHandler.close()
            return result

        return wrapper

    return _logging
