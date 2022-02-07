from matplotlib.pyplot import close
import yaml
#读取配置文件,返回信息
def readfile(local) ->dict: 
    with open(local,'r',encoding = 'utf-8') as file:
        result = yaml.full_load(file)
    file.close()
    return result

def upgradefile(local,id,group) -> bool:
    try:
        with open(local,'r',encoding = 'utf-8') as file:
            result = yaml.full_load(file)
        file.close()
        result[group]['id'].append(id)
        yaml.dump(result,open(local,'w',encoding='utf-8'))
        return True
    except:
        return False