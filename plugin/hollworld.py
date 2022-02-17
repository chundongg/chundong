import requests
import json

def forworld() -> str:
    r = requests.get('https://api.iyk0.com/60s')
    str_to_json = json.loads(r.text)
    return str_to_json['imageUrl']