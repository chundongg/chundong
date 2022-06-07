import requests

def forworld() -> str:
    r = requests.get('https://api.iyk0.com/60s')
    str_to_json = r.json()
    r.close()
    return str_to_json['imageUrl']