"""A module that gives static helper functions to plan and template"""
from template import Template
from entry import Entry
import CalcTime


def parseTextToEntries(text):
    entries = text.split("\n")
    entries = [Entry("00:00",e[6:],start=e[:5]) for e in entries if len(e) > 6] # hardcoded formatting
    
    for i,e in enumerate(entries):
        if not i +1 == len(entries):
            e.duration = CalcTime.substractTime(entries[i+1].start,e.start)
    return entries

def changeByEntries(plan_list,entry_list):
    new_plan_list = []
    for e in plan_list:
        index = doesEntryListContain(e,entry_list)
        if not index ==None:
            e.start = entry_list[index].start
            new_plan_list.append(e)
            entry_list = deleteListPart(index,entry_list,e)
    new_plan_list = new_plan_list + entry_list
    return new_plan_list


def deleteListPart(index,p_list,element):
    if isinstance(element,Template):
        l = len(element.step_list)
        p_list = p_list[:index] + p_list[index+l:]
    else:
        p_list.pop(index)
    return p_list

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