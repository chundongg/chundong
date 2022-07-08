import os
import yaml

def bind(mi,qq,qq_qun) -> bool:
    folder = os.path.exists("./genshin/{}".format(qq_qun))
    
    if not folder:
        os.makedirs("./genshin/{}".format(qq_qun))
        try:
            f = open("./genshin/{}/{}.yaml".format(qq_qun,qq_qun),'w',encoding='utf-8')
            f.close()
            data = {qq:mi}
            yaml.dump(data,open("./genshin/{}/{}.yaml".format(qq_qun,qq_qun),'w',encoding='utf-8'))
            return True
        except:
            return False
    else:
        if os.path.exists("./genshin/{}/{}.yaml".format(qq_qun,qq_qun)):
            try:
                with open("./genshin/{}/{}.yaml".format(qq_qun,qq_qun),'r',encoding = 'utf-8') as file:
                    data = yaml.full_load(file)
                    file.close()
                data[qq] = mi
                yaml.dump(data,open("./genshin/{}/{}.yaml".format(qq_qun,qq_qun),'w',encoding='utf-8'))
                return True
            except:
                return False
        else:
            try:
                f = open("./genshin/{}/{}.yaml".format(qq_qun,qq_qun),'w',encoding='utf-8')
                f.close()
                data = {qq:mi}
                yaml.dump(data,open("./genshin/{}/{}.yaml".format(qq_qun,qq_qun),'w',encoding='utf-8'))
                return True
            except:
                return False

def get_genshin(qq_qun,qq):
    try:
        with open("./genshin/{}/{}.yaml".format(qq_qun,qq_qun),'r',encoding = 'utf-8') as file:
            data = yaml.full_load(file)
            file.close()
        result = data[qq]
    except:
        result = False
    return result
