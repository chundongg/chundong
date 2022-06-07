import requests
from io import BytesIO
from PIL import Image
import uuid

def get_animepic() -> str:
    r = requests.get("http://iw233.cn/api/Random.php")
    image = Image.open(BytesIO(r.content))
    name = uuid.uuid4()
    image.save('./images/animepic/{}.jpg'.format(name))
    r.close()
    return name

def get_pixivpic() -> str:
    r = requests.get("https://pximg2.rainchan.win/rawimg")
    image = Image.open(BytesIO(r.content))
    name = r.url[r.url.find("img_id=")+7:]
    image.save('./images/pixivpic/{}.png'.format(name))
    r.close()
    return name