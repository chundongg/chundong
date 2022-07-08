import requests

def get_genshincard(uid):
    try:
        r = requests.get("https://api.daidr.me/apis/genshinUserinfo?uid={}&server=0".format(uid))
        result = r.json()['data']
    except:
        result = False
    return result