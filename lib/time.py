import time
from unittest import result

def localtime() -> str:
    localtime = time.localtime(time.time())
    if localtime.tm_hour < 6:
        result = '深夜好!'
    if localtime.tm_hour < 9:
        result = '早上好!'
    if localtime.tm_hour < 12:
        result = '上午好!'
    if localtime.tm_hour < 14:
        result = '中午好!'
    if localtime.tm_hour < 17:
        result = '下午好!'
    if localtime.tm_hour < 19:
        result = '傍晚好!'
    if localtime.tm_hour < 22:
        result = '晚上好!'
    else:
        result = '深夜好!'
    timenow = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    return result,timenow