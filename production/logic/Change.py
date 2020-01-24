"""A module that gives static helper functions to plan and template"""
from template import Template
from entry import Entry
import CalcTime
import re

def parseTextToEntries(text:str):
    entries = text.split("\n")
    return parseLinesToEntries(entries)

def parseLinesToEntries(lines:list):
    lines = [e for e in lines if len(e) > 6 and not re.match("^\d\d:\d\d",e) == None]
    entries = [Entry("00:00",e[6:],start=e[:5]) for e in lines] # hardcoded formatting
    
    for i,e in enumerate(entries):
        if not i +1 == len(entries):
            e.duration = CalcTime.substractTime(entries[i+1].start,e.start)
    return entries

def changeByEntries(plan_list,entry_list):
    new_plan_list = []
    for e in plan_list:
        index = doesEntryListContain(e,entry_list)
        if not index ==None:
            entry_list,new_element = deleteListPart(index,entry_list,e)
            new_plan_list.append(new_element)

    new_plan_list = new_plan_list + entry_list
    return new_plan_list


def deleteListPart(index,p_list,element):
    start = p_list[index].start
    if isinstance(element,Template):
        l = len(element.step_list)
        new_element = Template(element.theme)
        for e in p_list[index:index+l]:
            new_element.add(e)
        p_list[index+l-1].duration = element.step_list[-1].duration
        p_list = p_list[:index] + p_list[index+l:]
    else:
        new_element = p_list.pop(index)
    new_element.start = start
    return p_list,new_element

def doesEntryListContain(eOT:Entry,entry_list):
    if isinstance(eOT,Template):
        s_len =  len(eOT.step_list) 
        stop = len(entry_list) - s_len +1
        for index,e in enumerate( entry_list[:stop] ):
            if eOT.step_list == entry_list[index:index+s_len]:
                return index
        return None
    else:
        for index,e in enumerate(entry_list):
            if eOT == e:
                return index
        return None

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