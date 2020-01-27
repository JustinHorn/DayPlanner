from entry import Entry
from template import Template
from plan import Plan

from os import listdir
from os.path import isfile, join
import Change

def loadData(path:str):
    try:
        with open(path) as l:
            data = l.read()
        return data
    except RuntimeError as err:
        print("load Error:",err)
        return ""

def stringToTemplate(data:str):
    try:
        data = data.split("\n")
        theme = data[0]
        t = Template(theme)
        for e in data[1:]:
            [duration,theme] = [e[:5],e[6:]]
            t.add(Entry(duration,theme))
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
        with open(path,"w") as out:
            out.write(text)
    except IOError as io:
        print('An error occured in save:',io)


def loadText(path):
    try:
        with open(path,"r") as read:
            plan= read.read()
        return plan
    except IOError as io:
        print('An error occured in loadText',io)
        return "error in load plan with:"+path

def parsePlan(text:str):
    text = text.split("\n")
    plan = Plan(text[0])
    struc = genStructure(text[2:])

    content_start_index = len(struc)+3
    content = text[content_start_index:]

    entries = Change.parsePlanLinesToEntries(content)
    entrie_index = 0

    for e in struc:
        if e[2] == 1:
            plan.add(entries[entrie_index])
            entrie_index += 1
        elif e[2] >1:
            t = Template(e[1])
            t.start = e[0]
            c = e[2]
            for i in range(c):
                t.add(entries[entrie_index+i])
            entrie_index+=c
            plan.add(t)
    return plan

def genStructure(text:list):
    struc = []
    for line in text:
        eNSI = getEndNumberStartIndex(line)
        if not eNSI == 0:
            start = line[:5]
            theme = line[6:eNSI-1]
            count = int(line[eNSI:])
            struc.append((start,theme,count))
        else: 
            return struc
    print("everything parsed")
    return struc

def getEndNumberStartIndex(line:str):
    for i,char in enumerate(reversed(line)):
        if not char.isdigit():
            return -i
    return 0
