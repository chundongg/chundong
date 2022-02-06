import asyncio
from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
from graia.application import GraiaMiraiApplication, Group, Member
from graia.application.message.chain import MessageChain
from graia.application.message.elements.internal import Plain,Image

from lib.readfile import readfile
from lib.premssion import confirmpremssion
from lib.time import localtime

from plugin.randomfood import randomfood
from plugin.choicehelp import choicehelp
from plugin.animepic import get_animepic

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
                        Plain("{},{}\n╠#setgroup QQ号 权限组\n╠-------------------\n指令集:\n╠#随机吃饭 - 我也不知道吃啥啊！\n╠#帮我选择 选择A 选择B ...\n╠#二次元 - 杰哥注意上了你".format(data,user.name)
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
                            Plain("{},{}\n指令集:\n╠#随机吃饭 - 我也不知道吃啥啊！\n╠#帮我选择 - 啊对对对对！\n╠#二次元 - 杰哥注意上了你".format(data,user.name)
                            )
                        ]))
                    except:
                        await app.sendGroupMessage(group,message.create([
                            Plain("按理来说，你看不到这个，这是因为发生了未知错误")
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
    app.launch_blocking()