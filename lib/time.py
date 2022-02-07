import time

def localtime() -> str:
    localtime = time.localtime(time.time())
    if localtime.tm_hour < 24:
        result = '深夜好!'
    if localtime.tm_hour < 22:
        result = '晚上好!'
    if localtime.tm_hour < 19:
        result = '傍晚好!'
    if localtime.tm_hour < 17:
        result = '下午好!'
    if localtime.tm_hour < 14:
        result = '中午好!'
    if localtime.tm_hour < 12:
        result = '上午好!'
    if localtime.tm_hour < 9:
        result = '早上好!'
    if localtime.tm_hour < 6:
        result = '其实你还可以再睡会!'
    if localtime.tm_hour < 3:
        result = '这对我来说太早了点!'
    timenow = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    return result,timenow