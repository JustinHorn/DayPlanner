
from plan import Plan
from template import Template
from entry import Entry 
import ParseText

def parsePlanFromFileText(text):
    text = text.split("\n")
    theme = text[0]
    struc = generateStructure(text[2:])

    content_start_index = len(struc)+3
    content = text[content_start_index:]

    entries = ParseText.parsePlanLinesToEntries(content)

    plan = combineEntriesAndStructure(theme,struc,entries)
    return plan

def combineEntriesAndStructure(theme:str,structure:list,entries:list):
    entrie_index = 0
    plan = Plan(theme)
    for e in structure:
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


def generateStructure(lines:list):
    struc = []
    for line in lines:
        eNSI = ParseText.getEndNumberStartIndex(line)
        if not eNSI == 0:
            start = line[:5]
            theme = line[6:eNSI-1]
            count = int(line[eNSI:])
            struc.append((start,theme,count))
        else: 
            return struc
    print("everything parsed")
    return struc
