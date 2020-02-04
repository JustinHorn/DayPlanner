from entry import Entry
import CalcTime
import re


def parseTextToEntries(text:str,template=False):
    entries = text.split("\n")
    return parsePlanLinesToEntries(entries)

def parseTextToTemplateEntries(text):
    lines = text.split("\n")
    lines = filterFormat(lines)
    entries = [Entry(e[:5],e[6:]) for e in lines]
    return entries

def parsePlanLinesToEntries(lines:list):
    lines = filterFormat(lines) 
    entries = [Entry("00:00",e[6:],start=e[:5]) for e in lines] # hardcoded formatting
    
    for i,e in enumerate(entries):
        if not i +1 == len(entries):
            e.duration = CalcTime.substractTime(entries[i+1].start,e.start)
    return entries

def filterFormat(lines:list):
    return  [e for e in lines if len(e) > 6 and not re.match("^\d\d:\d\d",e) == None]


def getEndNumberStartIndex(line:str):
    for i,char in enumerate(reversed(line)):
        if not char.isdigit():
            return -i
    return 0
