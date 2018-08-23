# Python 2.7
from datetime import datetime
from contextlib import contextmanager


@contextmanager
def timer():
    # NOTE: The first run of a loop will take longer than the subsequent
    # loops because of caching mechanisms.
    start = datetime.now()
    yield
    end = datetime.now()
    print "Execution time: %s ms" % ((end - start).microseconds)
