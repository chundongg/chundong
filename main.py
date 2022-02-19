import asyncio
import re
from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
from graia.application import GraiaMiraiApplication, Group, Member,Friend
from graia.application.message.chain import MessageChain
from graia.application.message.elements.internal import Plain,Image

from lib.readfile import readfile
from lib.readfile import upgradefile
from lib.premssion import confirmpremssion
from lib.premssion import delpremssion
from lib.time import localtime

from plugin.randomfood import randomfood
from plugin.choicehelp import choicehelp
from plugin.animepic import get_animepic
from plugin.animepic import get_pixivpic
from plugin.bingpic import get_bingpic
from plugin.hollworld import forworld
from plugin.float import *
from plugin.aknowledge import get_knowledge
from plugin.qiandao import qiandao

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    bcc = Broadcast(loop=loop)
    authme = readfile('./setting/setting.yaml')
    connect_info = Session(
        host = authme['host'],
        account = authme['Bot']['account'],
        authKey = authme['Bot']['authKey'],
        websocket = authme['Bot']['websocket']
    )
    app = GraiaMiraiApplication(
        broadcast=bcc,
        connect_info=connect_info,
    )
    #help
    @bcc.receiver("GroupMessage")
    async def help(app: GraiaMiraiApplication, group: Group,user:Member,message:MessageChain):
        if message.asDisplay().startswith('#help'):
            data , timenow = localtime()
            flo = 0
            if confirmpremssion(user.id) >= 70:
                flo = 1
                try:
                    await app.sendGroupMessage(group,message.create([
                        Plain("{},{}\n╠#setgroup QQ号 权限组\n╠-------------------\n指令集:\n╠#随机吃饭 - 我也不知道吃啥啊！\n╠#帮我选择 选择A 选择B ...\n╠#二次元 - 杰哥注意上了你\n╠#bing - 必应每日一图\n╠#今日世界 - 60s读懂世界\n╠#漂流瓶 内容 - 投递漂流瓶\n╠#漂流瓶 - 捞一个漂流瓶\n╠#一言 - 一言\n╠#摇签 - 天不荒地不老\n╠#pixiv - 无瑟图".format(data,user.name)
                        )
                    ]))
                except:
                    await app.sendGroupMessage(group,message.create([
                        Plain("按理来说，你看不到这个，这是因为发生了未知错误")
                    ]))
            if flo == 0:
                if confirmpremssion(user.id) >= 10:
                    try:
                        await app.sendGroupMessage(group,message.create([
                            Plain("{},{}\n指令集:\n╠#随机吃饭 - 我也不知道吃啥啊！\n╠#帮我选择 选择A 选择B ...\n╠#二次元 - 杰哥注意上了你\n╠#bing - 必应每日一图\n╠#今日世界 - 60s读懂世界\n╠#漂流瓶 内容 - 投递漂流瓶\n╠#漂流瓶 - 捞一个漂流瓶\n╠#一言 - 一言\n╠#摇签 - 天不荒地不老\n╠#pixiv - 无瑟图".format(data,user.name)
                            )
                        ]))
                    except:
                        await app.sendGroupMessage(group,message.create([
                            Plain("按理来说，你看不到这个，这是因为发生了未知错误")
                        ]))
    #setgroup 
    @bcc.receiver("GroupMessage")
    async def help(app: GraiaMiraiApplication, group: Group,user:Member,message:MessageChain):
        if message.asDisplay().startswith('#setgroup '):
            if confirmpremssion(user.id) >= 70:
                word = re.sub("[^\w]", " ", message.asDisplay().replace("#setgroup ","")).split()
                if len(word) == 2:
                    try:
                        wl = int(word[0])
                    except:
                        await app.sendGroupMessage(group,message.create([
                            Plain("{},{}不是个有效的QQ号".format(user.name,word[0]))
                        ]))
                    else:
                        if wl >= 10000000:
                            if word[1] in ['admin','user','ban']:
                                try:
                                    if upgradefile('./setting/premssion.yaml',word[0],word[1]):
                                        if delpremssion(word[0],word[1]):
                                            await app.sendGroupMessage(group,message.create([
                                                Plain("{},已经成功将用户{}加入权限组{}".format(user.name,word[0],word[1]))
                                            ]))
                                        else:
                                            await app.sendGroupMessage(group,message.create([
                                                Plain("加入失败")
                                            ]))
                                    else:
                                        await app.sendGroupMessage(group,message.create([
                                            Plain("按理来说，你看不到这个，这是因为发生了未知错误")
                                        ]))
                                except:
                                    await app.sendGroupMessage(group,message.create([
                                        Plain("按理来说，你看不到这个，这是因为发生了未知错误")
                                    ]))
                            else:
                                await app.sendGroupMessage(group,message.create([
                                    Plain("{},权限组不存在\n权限组：[admin,user,ban]".format(user.name))
                                ]))
                        else:
                            await app.sendGroupMessage(group,message.create([
                                Plain("{},{}不是个有效的QQ号".format(user.name,word[0]))
                            ]))
                else:
                    await app.sendGroupMessage(group,message.create([
                        Plain("{},指令格式错误".format(user.name))
                    ]))
                
    #随机吃饭
    @bcc.receiver("GroupMessage")
    async def help(app: GraiaMiraiApplication, group: Group,user:Member,message:MessageChain):
        if message.asDisplay().startswith('#随机吃饭'):
            if confirmpremssion(user.id) >= 10:
                try:
                    await app.sendGroupMessage(group,message.create([
                        Plain("{},尝尝{}吧".format(user.name,randomfood()))
                    ]))
                except:
                    await app.sendGroupMessage(group,message.create([
                        Plain("按理来说，你看不到这个，这是因为发生了未知错误")
                    ]))
    #帮我选择 
    @bcc.receiver("GroupMessage")
    async def help(app: GraiaMiraiApplication, group: Group,user:Member,message:MessageChain):
        if message.asDisplay().startswith('#帮我选择 '):
            if confirmpremssion(user.id) >= 10:
                try:
                    await app.sendGroupMessage(group,message.create([
                        Plain("{},帮你选择:\n{}".format(user.name,choicehelp(user.name,message.asDisplay())))
                    ]))
                except:
                    await app.sendGroupMessage(group,message.create([
                        Plain("按理来说，你看不到这个，这是因为发生了未知错误")
                    ]))
    #二次元
    @bcc.receiver("GroupMessage")
    async def help(app: GraiaMiraiApplication, group: Group,user:Member,message:MessageChain):
        if message.asDisplay().startswith('#二次元'):
            if confirmpremssion(user.id) >= 10:
                try:
                    await app.sendGroupMessage(group,message.create([
                        Image.fromLocalFile('./images/animepic/{}.jpg'.format(get_animepic()))
                    ]))
                except:
                    await app.sendGroupMessage(group,message.create([
                        Plain("按理来说，你看不到这个，这是因为发生了未知错误")
                    ]))
    #bing
    @bcc.receiver("GroupMessage")
    async def help(app: GraiaMiraiApplication, group: Group,user:Member,message:MessageChain):
        if message.asDisplay().startswith('#bing'):
            if confirmpremssion(user.id) >= 10:
                try:
                    pic = get_bingpic()
                    picname = pic['title']
                    picurl = pic['imgurl']
                    await app.sendGroupMessage(group,message.create([
                        Plain(picname),Image.fromNetworkAddress(picurl)
                    ]))
                except:
                    await app.sendGroupMessage(group,message.create([
                        Plain("按理来说，你看不到这个，这是因为发生了未知错误")
                    ]))
    #今日世界
    @bcc.receiver("GroupMessage")
    async def help(app: GraiaMiraiApplication, group: Group,user:Member,message:MessageChain):
        if message.asDisplay().startswith('#今日世界'):
            if confirmpremssion(user.id) >= 10:
                try:
                    url = forworld()
                    await app.sendGroupMessage(group,message.create([
                        Image.fromNetworkAddress(url)
                    ]))
                except:
                    await app.sendGroupMessage(group,message.create([
                        Plain("按理来说，你看不到这个，这是因为发生了未知错误")
                    ]))
    #漂流瓶-delivery
    @bcc.receiver("GroupMessage")
    async def help(app: GraiaMiraiApplication, group: Group,user:Member,message:MessageChain):
        if message.asDisplay().startswith('#漂流瓶 '):
            if confirmpremssion(user.id) >= 10:
                word = re.sub("[^\w]", " ", message.asDisplay().replace("#漂流瓶 ","")).split()
                if len(word) == 1:
                    if word[0] != "#漂流瓶":
                        if delivery_floatbin(user.id,group.id,word[0]):
                            await app.sendGroupMessage(group,message.create([
                                Plain("{},你的漂流瓶已经漂向远方~~".format(user.name))
                            ]))
                        else:
                            await app.sendGroupMessage(group,message.create([
                                Plain("{},现在风浪不起，待会再试试吧".format(user.name))
                            ]))
                else:
                    await app.sendGroupMessage(group,message.create({
                        Plain("漂流瓶格式错误!\n格式:(#漂流瓶 内容)")
                    }))
    #漂流瓶-get
    @bcc.receiver("GroupMessage")
    async def help(app: GraiaMiraiApplication, group: Group,user:Member,message:MessageChain):
        if message.asDisplay().startswith('#漂流瓶'):
            if confirmpremssion(user.id) >= 10:
                word = re.sub("[^\w]", " ", message.asDisplay()).split()
                if len(word) == 1:
                    if word[0] == "漂流瓶":
                        try:
                            bin = get_floatbin()
                            if bin['data']['uin'].isdigit():
                                await app.sendGroupMessage(group,message.create([
                                    Plain("{},你捞到了一个来自{},群组{}的漂流瓶:\n\n{}\n\n{}".format(user.name,bin['data']['uin'],bin['data']['group'],bin['data']['msg'],bin['data']['Time']))
                                ]))
                            else:
                                await app.sendGroupMessage(group,message.create([
                                    Plain("{},哦吼，捞到了一个垃圾信息，已经自动屏蔽了".format(user.name))
                                ]))
                        except:
                            await app.sendGroupMessage(group,message.create([
                                Plain("{},没有捞到漂流瓶！".format(user.name))
                            ]))
    #摇签
    @bcc.receiver("GroupMessage")
    async def help(app: GraiaMiraiApplication, group: Group,user:Member,message:MessageChain):
        if message.asDisplay().startswith('#摇签'):
            if confirmpremssion(user.id) >= 10:
                try:
                    file = qiandao(user.id,user.name)
                    await app.sendGroupMessage(group,message.create([
                        Image.fromLocalFile('./plugin/qiandao_cache/{}.png'.format(file))
                    ]))
                except:
                    await app.sendGroupMessage(group,message.create([
                        Plain("按理来说，你看不到这个，这是因为发生了未知错误")
                    ]))
    #pixiv
    @bcc.receiver("GroupMessage")
    async def help(app: GraiaMiraiApplication, group: Group,user:Member,message:MessageChain):
        if message.asDisplay().startswith('#pixiv'):
            if confirmpremssion(user.id) >= 10:
                try:
                    picname = get_pixivpic()
                    await app.sendGroupMessage(group,message.create([
                        Plain("PID:{}".format(picname)),Image.fromLocalFile('./images/pixivpic/{}.png'.format(picname))
                    ]))
                except:
                    await app.sendGroupMessage(group,message.create([
                        Plain("图片服务器未响应")
                    ]))
    #一言
    @bcc.receiver("GroupMessage")
    async def help(app: GraiaMiraiApplication, group: Group,user:Member,message:MessageChain):
        if message.asDisplay().startswith('#一言'):
            if confirmpremssion(user.id) >= 10:
                try:
                    yiyan = get_knowledge()
                    await app.sendGroupMessage(group,message.create([
                        Plain("{}\n  ————{}".format(yiyan["hitokoto"],yiyan["from"]))
                    ]))
                except:
                    await app.sendGroupMessage(group,message.create([
                        Plain("按理来说，你看不到这个，这是因为发生了未知错误")
                    ]))
    app.launch_blocking()