"""
Changing the format of displayed messages
URL: https://docs.python.org/2/howto/logging.html#logging-basic-tutorial
"""
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')
