"""
Displaying date/time in messages
URL: https://docs.python.org/2/howto/logging.html#logging-basic-tutorial
"""
import logging
# Default format: ISO8601
# logging.basicConfig(format='%(asctime)s %(message)s')
# Formatted time
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')
