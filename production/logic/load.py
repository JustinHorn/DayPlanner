try:
    from entry import Entry
    from routine import Routine
    from plan import Plan
    import ParseText
    import Factory
except:
    from .entry import Entry
    from .routine import Routine
    from .plan import Plan
    from . import ParseText
    from . import Factory


from os import listdir
from os.path import isfile, join


def stringToRoutine(data:str):
    try:
        theme = data.split("\n")[0]
        t = Routine(theme)
        t.update(data[1:])
        return t
    except RuntimeError as err:
        print('parseData error',err)
        return routine("parseData error")

def loadRoutine(path):
    text = loadText(path)
    routine = Factory.parseRoutineFromFileText(text)
    return routine

def loadRoutineDir(directory:str):
    only_files = [f for f in listdir(directory) if isfile(join(directory,f))]
    only_routines =[f for f in only_files if not f.find("routine") == -1 ]
    routines = []
    for f in only_routines:
        routine = loadRoutine(join(directory,f))
        routines.append(routine)
    return routines

def save(path,text):
    try:
        with open(join(path),"w") as out:
            out.write(text)
    except IOError as io:
        print('An error occured in save:',io)


def loadText(path):
    try:
        path = join(path)
        with open(path,"r") as read:
            text= read.read()
        return text
    except IOError as io:
        print('An error occured in loadText path:',path,"|",io)
        return ""
