import requests
import json

def get_knowledge() -> dict:
    '''
    一言:https://hitokoto.cn/
    '''
    r = requests.get("https://v1.hitokoto.cn/")
    text = json.loads(r.text)
    return text