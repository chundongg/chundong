from .readfile import readfile
import yaml

def confirmpremssion(id) -> int:
    info = readfile('./setting/premssion.yaml')
    id = str(id)
    if id in info['admin']['id']:
        level = info['admin']['level']
    elif id in info['banner']['id']:
        level = info['banner']['level']
    else:
        level = info['user']['level']
    return level

def delpremssion(id,group) -> bool:
    try:
        info = readfile('./setting/premssion.yaml')
        grouplist = ['admin','user','banner']
        grouplist.remove(group)
        for i in grouplist:
            if id in info[i]['id']:
                info[i]['id'].remove(id)
        yaml.dump(info,open('./setting/premssion.yaml','w',encoding='utf-8'))
        return True
    except:
        return False