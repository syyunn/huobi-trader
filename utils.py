from datetime import datetime
import time


# def unix2reaadabletime(unix_timestamp):
#     return time.ctime(int(unix_timestamp))


def unix2datetime(unix_timestamp):
    return datetime.fromtimestamp(unix_timestamp)

