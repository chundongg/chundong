import yaml
#读取配置文件,返回信息
def readfile(local) ->dict: 
    with open(local,'r',encoding = 'utf-8') as file:
        result = yaml.full_load(file)
    file.close()
    return result