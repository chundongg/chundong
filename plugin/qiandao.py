from lib.time import localtime

import uuid
import json
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import requests

def qiandao(id,name) -> str:
    luckword = requests.get("https://api.fanlisky.cn/api/qr-fortune/get/{}".format(id))
    luckwordjson = json.loads(luckword.text)
    time,nowtime = localtime()
    picname = uuid.uuid4()
    getimage = requests.get("https://pximg2.rainchan.win/rawimg")
    picid = getimage.url[getimage.url.find("img_id=")+7:]

    #保存和获取图片大小
    image = Image.open(BytesIO(getimage.content))
    image.save('./images/qiandao/{}.png'.format(picname))
    imagesize = image.size

    size = imagesize[1]/942
    im = Image.new('RGB',(imagesize[0],imagesize[1]+int(imagesize[1]*5/40)),"#E6E6FA")

    im.paste(image)
    
    
    #字体处理
    fontvast = ImageFont.truetype(r'C:\Windows\Fonts\STXINWEI.TTF',int(48*size))
    fontmid = ImageFont.truetype(r'C:\Windows\Fonts\STXINWEI.TTF',int(36*size))
    fontnegliable = ImageFont.truetype(r'C:\Windows\Fonts\STXINWEI.TTF',int(18*size))
    draw = ImageDraw.Draw(im)

    draw.text((imagesize[0]*1/10,imagesize[1]),time+name,font=fontvast,fill="#000000")
    draw.text((imagesize[0]*5/10,imagesize[1]*21/20),luckwordjson["data"]["luckyStar"],font=fontmid,fill="#000000")

    draw.text((imagesize[0]*18/20,imagesize[1]*24/22),"@小椿",font=fontnegliable,fill="#000000")
    draw.text((imagesize[0]*2/20,imagesize[1]*24/22),"PID:"+picid,font=fontnegliable,fill="#000000")

    #保存签到图片方便调用
    save = 'save'
    im.save('./plugin/qiandao_cache/save.png')

    return save