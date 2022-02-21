import requests
import json

def get_floatbin() -> dict:
    r = requests.get("https://api.iyk0.com/drift/?type=2")
    bin = json.loads(r.text)
    return bin

text = []
for i in range(100):
    try:
        bin = get_floatbin()
        print(bin['data']['msg'])
        lay = int(input("(垃圾信息:1,非垃圾信息:0)input:"))
        text.append((bin['data']['msg'],lay))
    except:
        pass

print(text)