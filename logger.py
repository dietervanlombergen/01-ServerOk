# Imports
import logging

# Consts
LOGFILE = "log/server.log"
LOGNAME = "serverLogger"


# Create a logger
logger = logging.getLogger(LOGNAME)
logger.setLevel(logging.DEBUG)

# Create a file handler
fh = logging.FileHandler(LOGFILE)
fh.setLevel(logging.DEBUG)

# Create a console handler
# ch = logging.StreamHandler()
# ch.setLevel(logging.ERROR)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
#ch.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(fh)
#logger.addHandler(ch)

# Log some messages
# logger.debug('Debug message')
# logger.info('Info message')
# logger.warning('Warning message')
# logger.error('Error message')
# logger.critical('Critical message')

def get_log():
    return logger

