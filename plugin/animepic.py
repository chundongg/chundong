import requests
from io import BytesIO
from PIL import Image
import uuid

def get_animepic():
    r = requests.get("http://iw233.cn/api/Random.php")
    image = Image.open(BytesIO(r.content))
    name = uuid.uuid4()
    image.save('./images/animepic/{}.jpg'.format(name))
    return name