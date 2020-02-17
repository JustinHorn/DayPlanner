from entry import Entry
import CalcTime
import re


def parseTextToEntries(text:str,template=False):
    entries = text.split("\n")
    return to_planEntries(entries)

def to_templateEntries(text):
    lines = text.split("\n")
    lines = filterFormat(lines)
    entries = [Entry(e[:5],e[6:]) for e in lines]
    return entries

def to_planEntries(lines:list):
    lines = filterFormat(lines) 
    entries = [makePlanEntry(e) for e in lines] # hardcoded formatting
    
    for i,e in enumerate(entries):
        if not i +1 == len(entries):
            if e.duration == "00:00":
                e.duration = CalcTime.substractTime(entries[i+1].start,e.start)
    return entries

def makePlanEntry(line:str):
    if re.match(".*\d\d:\d\d$",line):
        return Entry(line[-5:],line[6:-5],start=line[:5])
    else:
        return Entry("00:00",line[6:],start=line[:5])       

def filterFormat(lines:list):
    return  [e for e in lines if is_line_entry(e)]

def is_line_entry(line):
    return len(line) > 6 and re.match("^\d\d:\d\d",line)

def insertTime(plan,source,index):
    lines = source.split("\n")
    count = 0
    for i,l in enumerate(lines):
        if i == index and count > 0:
            e = plan.getEntryAtIndex(count-1)
            lines[index] = CalcTime.addTime(e.start,e.duration)+" "
        elif is_line_entry(l):
            count +=1
    return join_str_list(lines)

def join_str_list(lines:list):
    string = ""
    for l in lines[:-1]:
        string = string + l + "\n"
    string+= lines[-1]
    return string
