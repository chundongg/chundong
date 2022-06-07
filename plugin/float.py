import requests

def delivery_floatbin(user,group,text) -> bool:
    try:
        r = requests.get("https://api.iyk0.com/drift/?type=1&msg={}&uin={}&group={}".format(text,user,group))
        r.close()
    except:
        return False
    else:
        return True

def get_floatbin() -> dict:
    r = requests.get("https://api.iyk0.com/drift/?type=2")
    bin = r.json()
    r.close()
    return bin