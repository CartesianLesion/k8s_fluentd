# log.py


from logging import getLogger, StreamHandler, Formatter, DEBUG
from logging.handlers import RotatingFileHandler


logger = getLogger('log_app')
logger.setLevel(DEBUG)

log_path = 'app.log'

rotating_file_handler = RotatingFileHandler(log_path,
                                            maxBytes=1024 * 1024,
                                            backupCount=10)
rotating_file_handler.setLevel(DEBUG)

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = Formatter(log_format)
rotating_file_handler.setFormatter(formatter)

logger.addHandler(rotating_file_handler)

