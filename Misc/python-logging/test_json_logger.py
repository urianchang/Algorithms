import logging
import json
from pythonjsonlogger import jsonlogger

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['test'] = "TESTING"
    def parse(self):
        # self._fmt = ['asctime', 'created', 'filename', 'funcName', 'levelname', 'levelno', 'lineno', 'module',
        #              'message', 'name', 'process', 'processName', 'thread', 'threadName']
        self._fmt = ['levelname', 'test']
        return self._fmt
    def formatException(self, exc_info):
        emsg = super(CustomJsonFormatter, self).formatException(exc_info)
        traceback = '\n'.join(emsg.splitlines()[1:-1]).strip()
        reason = emsg.splitlines()[-1]
        edict = {'traceback': traceback, 'reason': reason}
        return edict

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logHandler = logging.StreamHandler()
# formatter = jsonlogger.JsonFormatter("""(asctime) (created) (filename)
#                                         (funcName) (levelname) (levelno)
#                                         (lineno) (module) (message) (name)
#                                         (process) (processName) (thread) (threadName)""")
formatter = CustomJsonFormatter()
# def json_translate(obj):
#     if isinstance(obj, MyClass):
#         return {"special": obj.special}
#
# formatter = jsonlogger.JsonFormatter(json_default=json_translate)

logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

'''Logging Stuff...'''
# logger.debug("This is a debug message")
# logger.info("This is an info message")
# logger.warning("This is a warning message")

try:
    1/0
except Exception:
    logger.exception("Some exception 1")

# try:
#     2/0
# except Exception:
#     logger.exception("Some exception 2")

# logger.info({"special": "value", "run": 12})
# logger.info("classic message", extra={"special": "value", "run": 12})
