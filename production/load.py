from entry import Entry
from template import Template
from os import listdir
from os.path import isfile, join

def loadData(path:str):
    with open(path) as l:
        data = l.read()
    return data

def parseData(data:str):
    data = data.split("\n")
    theme = data[0]
    t = Template(theme)
    for e in data[1:]:
        [duration,theme] = e.split("|")
        t.add(Entry(duration,theme))
    return t

def loadTemplate(path):
    data = loadData(path)
    template = parseData(data)
    return template

def loadTemplateDir(directory:str):
    only_files = [f for f in listdir(directory) if isfile(join(directory,f))]
    only_templates =[f for f in only_files if not f.find("template") == -1 ]
    templates = []
    for f in only_templates:
        temp = loadTemplate(join(directory,f))
        templates.append(temp)
    return templates

