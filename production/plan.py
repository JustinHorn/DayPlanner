from entry import Entry
from template import Template
from calcTime import *

class Plan(Template):

    STANDARD_START = "07:00"

    def __init__(self,date:str, start=None,the_list=[]):
        super().__init__(date)
        if start == None:
            self.start = Plan.STANDARD_START
        else:
            self.start = start
        self.end = self.start
        if len(the_list) > 0:
            for e in the_list:
                self.add(e)

    def add(self,tempOrEntry):
        eOT = tempOrEntry.clone()
        self.setStart(eOT)
        self.the_list.append(eOT)
        return eOT
    
    def remove(self,index):
        element = self.the_list.pop(index)
        self.end = element.start
        self.updateStarts(index=index)
        return element
    
    def removeAppointment(self,startTime:str):
        for index,eOT in enumerate(the_list):
            if eOT.start == startTime:
                return self.the_list.pop(index)
        return None

    def updateStarts(self,index=0):
        for e in self.the_list[index:]:
            self.setStart(e)

    def setStart(self,eOT):
        if isinstance(eOT,Template):
            eOT.start = self.end
            t_list = eOT.the_list
            for e in t_list:
                self.setElementStart(e)
        else:
            self.setElementStart(eOT)

    def setElementStart(self,entry):
        entry.start = self.end
        self.end = addTime(self.end,entry.duration)

    def setPlanStart(self,start):
        self.start = start
        self.end = start
        for e in self.the_list:
            self.setStart(e)

    def getText(self):
        string:str =""
        for tOE in self.the_list:
            if isinstance(tOE,Template):
                for e in tOE.the_list:
                    string = string + e.toString()
            else:
                e = tOE
                string = string + e.toString()
        return string
                
