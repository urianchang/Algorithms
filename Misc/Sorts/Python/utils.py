# Python 2.7
from datetime import datetime
from contextlib import contextmanager


@contextmanager
def timer():
    start = datetime.now()
    yield
    end = datetime.now()
    print "Execution time: %s ms" % (end - start).microseconds
