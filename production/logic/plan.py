from entry import Entry
from template import Template
import calcTime 

class Plan(Template):

    STANDARD_START = "07:00"

    def __init__(self,date:str, start=None,step_list=[]):
        super().__init__(date)
        if start == None:
            self.start = Plan.STANDARD_START
        else:
            self.start = start
        self.end = self.start
        if len(step_list) > 0:
            for e in step_list:
                self.add(e)

    def add(self,tempOrEntry):
        eOT = tempOrEntry.clone()
        self.setStart(eOT)
        self.step_list.append(eOT)
        return eOT
    
    def remove(self,index):
        element = self.step_list.pop(index)
        self.end = element.start
        self.updateStarts(index=index)
        return element
    
    def removeAppointment(self,startTime:str):
        for index,eOT in enumerate(step_list):
            if eOT.start == startTime:
                return self.step_list.pop(index)
        return None

    def updateStarts(self,index=0):
        for e in self.step_list[index:]:
            self.setStart(e)

    def setStart(self,eOT):
        if isinstance(eOT,Template):
            eOT.start = self.end
            t_list = eOT.step_list
            for e in t_list:
                self.setElementStart(e)
        else:
            self.setElementStart(eOT)

    def setElementStart(self,entry):
        entry.start = self.end
        self.end = calcTime.addTime(self.end,entry.duration)

    def setPlanStart(self,start):
        self.start = start
        self.end = start
        for e in self.step_list:
            self.setStart(e)

    def getText(self):
        string:str =""
        for tOE in self.step_list:
            if isinstance(tOE,Template):
                for e in tOE.step_list:
                    string = string + e.start +" "+e.theme+" \n"
            else:
                e = tOE
                string = string + e.start +" "+e.theme+" \n"
        return string
                
    def splitTemplate(self,template_index,split_point):
        t = self.step_list.pop(template_index)
        t1,t2 = t.split(split_point)
        self.step_list.insert(template_index,t2)
        self.step_list.insert(template_index,t1)
        t1.start = t.start
        t2.start = calcTime.addTime(t.start,t1.duration)
        return t

    
    def update(self,update_text):
        entries = Plan.parseTextToEntries(update_text)
        
        self.step_list = Plan.changeByEntries(self.step_list,entries)
        self.step_list.sort(key=Plan.sort)
        self.step_list = Plan.formatList(self.step_list)
        self.end = self.step_list[0].start
        self.updateStarts()
    
    @staticmethod
    def parseTextToEntries(text):
        entries = text.split("\n")
        entries = [Entry("00:00",e[6:],start=e[:5]) for e in entries] # hardcoded formatting
        
        for i,e in enumerate(entries):
            if not i +1 == len(entries):
                e.duration = calcTime.substractTime(entries[i+1].start,e.start)
        return entries

    @staticmethod
    def changeByEntries(plan_list,entry_list):
        new_plan_list = []
        for e in plan_list:
            index = Plan.doesEntryListContain(e,entry_list)
            if not index ==None:
                e.start = entry_list[index].start
                new_plan_list.append(e)
                entry_list = Plan.deleteListPart(index,entry_list,e)
        new_plan_list = new_plan_list + entry_list
        return new_plan_list

    @staticmethod
    def sort(e):
        return e.start

    @staticmethod
    def doesEntryListContain(eOT:Entry,entry_list):
        if isinstance(eOT,Template):
            step_list = eOT.step_list
            s_len = len(step_list)
            stop = len(entry_list) - s_len +1
            for index,e in enumerate( entry_list[:stop] ):
                for s_i, t_e in enumerate( step_list):
                    element =  entry_list[s_i+index]
                    if not( element ==t_e or (element.duration =="00:00" and element.theme == t_e.theme)):
                        break
                    elif s_i+1 == s_len:
                        return index
            return None
        else:
            for index,e in enumerate(entry_list):
                if (eOT == e) or (e.duration =="00:00" and e.theme == eOT.theme):
                    return index
            return None

    @staticmethod
    def deleteListPart(index,p_list,element):
        if isinstance(element,Template):
            l = len(element.step_list)
            p_list = p_list[:index] + p_list[index+l:]
        else:
            p_list.pop(index)
        return p_list

    @staticmethod
    def formatList(plan_list):
        entries_collected = []
        new_list = []
        for e in plan_list:
            if not isinstance(e,Template):
                entries_collected.append(e)
            else:
                if len(entries_collected) >=2:
                    new_list.append(Plan.entriesToTemplate(entries_collected))
                else:
                    new_list = new_list + entries_collected

                new_list.append(e)
                entries_collected = []

        if len(entries_collected) >=2:
            new_list.append(Plan.entriesToTemplate(entries_collected))
        else:
            new_list = new_list + entries_collected
        return new_list
    
    @staticmethod
    def entriesToTemplate(entries):
        t = Template("...")
        t.start = entries[0].start
        for entry in entries:
            t.add(entry)
        return t
