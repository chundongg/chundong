from graia.application.event.messages import FriendMessage, GroupMessage,TempMessage
from graia.application import BotMessage, Friend, GraiaMiraiApplication, Group, Member
from graia.broadcast import Broadcast, DispatcherInterface
from graia.application.message.chain import MessageChain
from graia.application.message.elements.internal import Image, Plain

from .readfile import readfile


def allmessagechain(bcc: Broadcast):
    @bcc.receiver(GroupMessage)
    async def sendmessage(event:GroupMessage,user:Member,group:Group):
        info = await readfile('../setting/premssion.yaml')
        if user.id in info['admin']['id']:
            level = info['admin']['level']
        elif user.id in info['banner']['id']:
            level = info['banner']['level']
        else:
            level = info['user']['leve']
        request = 1
        result = 1
        async def eachsendmessage(
            app: GraiaMiraiApplication,
            message: MessageChain,
            group: Group,
            user: Member,
            level=level,
            request=request,
            result=result
        ):
            if level >= 10:
                if message.asDisplay().startswith(request):
                    try:
                        await app.sendGroupMessage(group,MessageChain.create([
                            Plain("{},{}".format(user.id,result))
                        ]))
                    except:
                        await app.sendGroupMessage()
    @bcc.receiver(FriendMessage)
    async def sendmessage(event:FriendMessage,user:Friend):
        info = await readfile('../setting/premssion.yaml')
        if user.id in info['admin']['id']:
            level = info['admin']['level']
        elif user.id in info['banner']['id']:
            level = info['banner']['level']
        else:
            level = info['user']['leve']
        bcc.postEvent(
            FriendMessage(

            )
        )
    @bcc.receiver(TempMessage)
    async def sendmessage(event:TempMessage,user:Member):
        info = await readfile('../setting/premssion.yaml')
        if user.id in info['admin']['id']:
            level = info['admin']['level']
        elif user.id in info['banner']['id']:
            level = info['banner']['level']
        else:
            level = info['user']['leve']
        bcc.postEvent(
            TempMessage(

            )
        )