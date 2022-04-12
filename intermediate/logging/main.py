import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs app.log1, app.log2, etc.
handler = TimedRotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Hello, world!')
#import traceback

#try:
#    a = [1, 2, 3]
#    val = a[4]
#except IndexError as e:
#    logging.error("The error is %s", traceback.format_exc())



# import logging.config
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                    datefmt='%m/%d/%Y %H:%M:S')
# import helper 

#logging.config.fileConfig('logging.conf')

# logger = logging.getLogger(__name__)
#logger = logging.getLogger(simpleExample)
#logger.debug('this is a debug message')

"""
# create handler 
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and the format 
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')
"""
