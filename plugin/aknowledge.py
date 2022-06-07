import requests

def get_knowledge() -> dict:
    '''
    一言:https://hitokoto.cn/
    '''
    r = requests.get("https://v1.hitokoto.cn/")
    text = r.json()
    r.close()
    return text