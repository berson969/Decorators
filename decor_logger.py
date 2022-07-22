import logging
from functools import wraps

# WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__doc__')
# WRAPPER_UPDATES = ('__dict__',)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fileHandler = logging.FileHandler('logs/logs.log')
fileHandler.setFormatter(logging.Formatter(fmt='%(asctime)s: %(message)s')) # attrbs LogRecord
logger.addHandler(fileHandler)

# streamHandler = logging.StreamHandler()
# streamHandler.setFormatter(logging.Formatter(fmt='%(asctime)s: %(message)s')) # attrbs LogRecord
# logger.addHandler(streamHandler)


def decor_logging(func):
    
    @wraps(func) #, assigned = WRAPPER_ASSIGNMENTS, updates=WRAPPER_UPDATES)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # logger.info(f'Function name: {func.__name__}')
        # logger.info(f'Check2 {func.__doc__}')
        # logger.info(f'Check3 {func.__dict__}')
        # logger.info(f'Launch module {func.__module__}')
        logger.info(f'Log: {fileHandler.baseFilename[-14::1]} FuncName: {func.__name__}: Result {result} Title {str(args[0])[:90]}')
        # logger.info(f'Title {str(args[0])[:90]}')
        # logger.info(f'Logfile name {fileHandler.baseFilename[-14::1]}')
        return result

    return wrapper