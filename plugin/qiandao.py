from matplotlib import image
from numpy import imag
from .aknowledge import get_knowledge

from ..lib.time import localtime

import os
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import requests

def qiandao(id) -> bool:
    aknowledge = get_knowledge()
    luckword = requests.get("https://api.fanlisky.cn/api/qr-fortune/get/{}".format(id))
    time,nowtime = localtime()
    getimage = requests.get("https://api.mtyqx.cn/api/random.php")

    image = Image.open(BytesIO(getimage.content))
    image.save('./images/bingpic/{}.jpg'.format(nowtime))