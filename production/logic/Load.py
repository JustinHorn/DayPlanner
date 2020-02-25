try:
    from entry import Entry
    from template import Template
    from plan import Plan
    import ParseText
    import Factory
except:
    from .entry import Entry
    from .template import Template
    from .plan import Plan
    from . import ParseText
    from . import Factory


from os import listdir
from os.path import isfile, join


def stringToTemplate(data:str):
    try:
        theme = data.split("\n")[0]
        t = Template(theme)
        t.update(data[1:])
        return t
    except RuntimeError as err:
        print('parseData error',err)
        return Template("parseData error")

def loadTemplate(path):
    text = loadText(path)
    template = Factory.parseTemplateFromFileText(text)
    return template

def loadTemplateDir(directory:str):
    only_files = [f for f in listdir(directory) if isfile(join(directory,f))]
    only_templates =[f for f in only_files if not f.find("template") == -1 ]
    templates = []
    for f in only_templates:
        temp = loadTemplate(join(directory,f))
        templates.append(temp)
    return templates

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
