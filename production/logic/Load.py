from entry import Entry
from template import Template
from plan import Plan

from os import listdir
from os.path import isfile, join
import Change
import ParseText

def loadData(path:str):
    try:
        with open(join(path)) as l:
            data = l.read()
        return data
    except RuntimeError as err:
        print("load Error:",err)
        return ""

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

