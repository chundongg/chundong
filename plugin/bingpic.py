import requests
import random
from io import BytesIO
from PIL import Image

def get_bingpic() ->list:
    r = requests.get("https://api.iyk0.com/mryt/")
    str_to_json = r.json()
    r.close()
    pic = random.choice(str_to_json['data'])
    picname = pic['title']
    fixname = picname.replace('/','-')
    picurl = pic['imgurl']
    picurl2 = requests.get(picurl)
    image = Image.open(BytesIO(picurl2.content))
    image.save('./images/bingpic/{}.jpg'.format(fixname))
    picurl2.close()
    return pic