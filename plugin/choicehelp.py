import random
import re

def choicehelp(name,text:str) ->str:
    word = re.sub("[^\w]", " ", text.replace("#帮我选择 ","")).split()
    result = random.choice(word)
    return result