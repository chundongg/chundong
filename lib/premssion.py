from .readfile import readfile

def confirmpremssion(id):
    info = readfile('./setting/premssion.yaml')
    id = str(id)
    if id in info['admin']['id']:
        level = info['admin']['level']
    elif id in info['banner']['id']:
        level = info['banner']['level']
    else:
        level = info['user']['level']
    return level