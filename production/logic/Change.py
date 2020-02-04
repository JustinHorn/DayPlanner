"""A module that gives static helper functions to plan and main"""

from template import Template
from entry import Entry
import CalcTime
import re


def mergeListToEntries(plan_list,entry_list):
    merge = []
    for e in plan_list:
        contains, index = doesEntryListContain(e,entry_list)
        if contains:
            new_element = getElement(index,entry_list,e)
            entry_list = shortenList(index,entry_list,e)
            merge.append(new_element)

    merge = merge + entry_list
    return merge

def doesEntryListContain(eOT:Entry,entry_list):
    if isinstance(eOT,Template):
        return template_contain(eOT,entry_list)
    else:
        index = None
        if eOT in entry_list:
            index = entry_list.index(eOT)
        return (not index == None),index

def getElement(index,p_list,element):
    if isinstance(element,Template):
        ele = createNewTemplate(index,p_list,element)
    else:
        ele = p_list[index] 

    ele.start= p_list[index].start 
    return ele

def createNewTemplate(index,p_list,old_temp):
    entries = p_list[index:index+len(old_temp.step_list)]
    new_temp = Template(old_temp.theme)
    new_temp.addAll(entries)
    new_temp.step_list[-1].duration = old_temp.step_list[-1].duration
    return new_temp

def template_contain(template,entry_list):
    s_len =  len(template.step_list) 
    stop = len(entry_list) - s_len +1
    for index,e in enumerate( entry_list[:stop] ):
        if template.step_list == entry_list[index:index+s_len]:
            return True,index
    return False,None

def shortenList(index,p_list,element):
    if isinstance(element,Template):
        p_list = template_shortenList(index,p_list,len(element.step_list))
    else:
        p_list.pop(index)
    return p_list


###change template list
def template_shortenList(index,p_list,length):
    p_list = p_list[:index] + p_list[index+length:]
    return p_list

def sortByStart(e):
    return e.start


def formatList(plan_list):
    entries = []
    new_list = []
    for e in plan_list:
        if not isinstance(e,Template):
            entries.append(e)
        else:
            new_list = addEntriesToList(new_list,entries)
            new_list.append(e)
            entries = []

    return addEntriesToList(new_list,entries)

def addEntriesToList(new_list,entries):
    if more(entries,than=1):
        new_list.append(entriesToTemplate(entries))
    else:
        new_list = new_list + entries
    return new_list

def more(collection,than=0):
    return len(collection) > than


def entriesToTemplate(entries):
    t = Template("...")
    t.start = entries[0].start
    for entry in entries:
        t.add(entry)
    return t