"""
Logging to a file and specifying args in command line
URL: https://docs.python.org/2/howto/logging.html#logging-basic-tutorial
"""
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--level')
loglevel = parser.parse_args().level
numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)
logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
