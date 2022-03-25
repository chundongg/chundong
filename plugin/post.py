import requests
import json
import random
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
    timenow = time.strftime("%Y/%m/%d %H/%M", time.localtime())
    return result,timenow


def post(id,name) -> str:
    context = requests.get("https://v1.hitokoto.cn/")
    context_text = json.loads(context.text)
    luckstar = requests.get("https://api.fanlisky.cn/api/qr-fortune/get/{}".format(id))
    luckstar_text = json.loads(luckstar.text)
    picurl = requests.get("https://api.iyk0.com/mryt/")
    picurl_text = json.loads(picurl.text)
    pic = random.choice(picurl_text['data'])
    url = pic["imgurl"]
    time,nowtime = localtime()
    tip = "@小c、小d"
    posturl = "https://tenapi.cn/poster/?qrcode=今日运势:{}&title={} {}&content={}&site={}&info={}&author={}&pic={}".format(luckstar_text["data"]["signText"],time,name,context_text["hitokoto"],nowtime,tip,context_text["from"],url)
    return posturl