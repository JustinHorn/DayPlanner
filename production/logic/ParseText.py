try:
    from entry import Entry
    import CalcTime
    import re
except:
    from .entry import Entry
    from . import CalcTime
    import re

def templateText_toEntries(text):
    lines = text.split("\n")
    lines = filterEntries(lines)
    entries = [Entry(e[:5],e[6:]) for e in lines]
    return entries

def planText_toEntries(text:str):
    entries = text.split("\n")
    return planLines_toEntries(entries)

def planLines_toEntries(lines:list):
    lines = filterEntries(lines) 
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

def filterEntries(lines:list):
    return  [e for e in lines if is_line_entry(e)]

def is_line_entry(line):
    return len(line) > 6 and re.match("^\d\d:\d\d",line)


def insertEndTime(plan,text,index):
    # finds last entrie line index in text and plan, then  inserts time, 
    lines = text.split("\n")
    entry_index = getEntryNumber_beforeLine(lines,index) -1
    entry = plan.getEntryAtIndex(entry_index)
    lines[index] = entry.getEnd()
    return join_str_list(lines)



 

def getEntryNumber_beforeLine(text,line_index):
    if not isinstance(text,list):
        lines = text.split("\n")
    else:
        lines = text
    lines[line_index]
    count_entries= 0
    for l_index,l in enumerate(lines):
        if l_index == line_index:
            return count_entries
        elif is_line_entry(l):
            count_entries +=1
    raise Exception("code should have never come so far")

def join_str_list(lines:list):
    string = ""
    for l in lines[:-1]:
        string = string + l + "\n"
    string+= lines[-1]
    return string
