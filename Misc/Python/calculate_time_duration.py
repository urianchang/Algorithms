from datetime import datetime 
from time import sleep
import pytz

starttime_string = pytz.utc.localize(datetime.utcnow()).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
starttime = datetime.strptime(starttime_string, '%Y-%m-%dT%H:%M:%S.%fZ')
sleep(1)
endtime_string = pytz.utc.localize(datetime.utcnow()).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
endtime = datetime.strptime(endtime_string, '%Y-%m-%dT%H:%M:%S.%fZ')

print((endtime-starttime).total_seconds())