from entry import Entry
from template import Template
from os import listdir
from os.path import isfile, join

def loadData(path:str):
    with open(path) as l:
        data = l.read()
    return data

def stringToTemplate(data:str):
    try:
        data = data.split("\n")
        theme = data[0]
        t = Template(theme)
        for e in data[1:]:
            [duration,theme] = [e[:5],e[6:]]
            t.add(Entry(duration,theme))
        return t
    except:
        print('parseData error')
        return Template("parseData error")

def loadTemplate(path):
    data = loadData(path)
    template = stringToTemplate(data)
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
        with open(path,"w") as out:
            out.write(text)
    except IOError:
        print('An error occured in save')


def loadPlan(path):
    try:
        with open(path,"r") as read:
            plan= read.read()
        return plan
    except IOError:
        print('An error occured in loadPlan')
        return "error in load plan with:"+path