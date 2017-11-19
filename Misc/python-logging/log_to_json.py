import logging
import json

class JsonHandler(logging.FileHandler):
    def __init__(self, file):
        logging.FileHandler.__init__(self, file)
        self.file = file
    def emit(self, record):
        # log_obj = format(record)  # Why doens't it use the custom Formatter?
        log_obj = log_to_dict(record)
        with open(self.file, 'r+') as json_file:
            d = json.load(json_file)
            d['logs'].append(log_obj)
            json_file.seek(0)
            json.dump(d, json_file, indent=4)
            json_file.truncate()

def log_to_dict(record):
    data = {'name': record.name,
            'levelname': record.levelname,
            'pathname': record.pathname,
            'lineno': record.lineno,
            'msg': record.msg,
            'args': record.args,
            'exc_info': record.exc_info}
    return data

class DictFormatter(logging.Formatter):
    def __init__(self):
        super(DictFormatter, self).__init__()
        # logging.Formatter.__init__(self, *args, **kwargs)
    def format(self, record):
        # print record
        data = {'name': record.name,
                'levelname': record.levelname,
                'pathname': record.pathname,
                'lineno': record.lineno,
                'msg': record.msg,
                'args': record.args,
                'exc_info': record.exc_info}
        return data

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
df = DictFormatter()
# h1 = logging.StreamHandler()
# h1.setLevel(logging.DEBUG)
# h2 = logging.FileHandler('example.log')
# h2.setLevel(10)
# h1.setFormatter(df)
# h2.setFormatter(df)
# logger.addHandler(h1)
# logger.addHandler(h2)
h = JsonHandler('test.json')
h.setLevel(logging.DEBUG)
# h.setFormatter(df)    # Doesn't seem to work
logger.addHandler(h)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")

# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")

"""
filename='test.json'
level=logging.DEBUG
FORMAT = json.dumps({'asctime': '%(asctime)s', 'name': '%(name)s', 'levelname': '%(levelname)s', 'message': '%(message)s'})

logging.basicConfig(format=FORMAT, filename=filename, level=level)
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
"""
