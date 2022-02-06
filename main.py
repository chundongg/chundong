import asyncio
from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session

from lib.readfile import readfile

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
    app.launch_blocking()