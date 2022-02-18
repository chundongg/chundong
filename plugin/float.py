from aiohttp import request
import requests
import json

def delivery_floatbin(user,group,text) -> bool:
    try:
        r = requests.get("https://api.iyk0.com/drift/?type=1&msg={}&uin={}&group={}".format(text,user,group))
    except:
        return False
    else:
        return True

def get_floatbin() -> dict:
    r = requests.get("https://api.iyk0.com/drift/?type=2")
    bin = json.loads(r.text)
    return bin