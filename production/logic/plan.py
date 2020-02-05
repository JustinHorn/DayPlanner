from entry import Entry
from template import Template
import CalcTime 
from updater import Updater
from formatStructure import FormatStructure

import ParseText

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
        self.updateStarts(element.start,index)
        return element
    
    def removeAppointment(self,startTime:str):
        for index,eOT in enumerate(step_list):
            if eOT.start == startTime:
                return self.step_list.pop(index)
        return None

    def updateStarts(self,startTime,index):
        if index < len(self.step_list):
            self.end = startTime
            for e in self.step_list[index:]:
                self.setStart(e)
        else:
            print("Index",index,"out of range: plan - updateStars")

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
        self.end = CalcTime.addTime(self.end,entry.duration)

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
                    string = string + e.start +" "+e.theme+"\n"
            else:
                e = tOE
                string = string + e.start +" "+e.theme+"\n"
        return string

    def getStructureInText(self):
        structure:str =""
        for e in self.step_list:
            structure=structure+ e.getStartTheme() + " "+str(e.count)+"\n"
        return structure

    def getFileText(self):
        name_and_elements = self.theme+"\n"+"Structure:\n"+self.getStructureInText()
        content = "Content:\n"+self.getText()
        return name_and_elements + content

    def splitTemplate(self,template_index,split_point):
        t = self.step_list.pop(template_index)
        t1,t2 = t.split(split_point)
        self.step_list.insert(template_index,t2)
        self.step_list.insert(template_index,t1)
        t1.start = t.start
        t2.start = CalcTime.addTime(t.start,t1.duration)
        return t

    def update(self,update_text):
        entries = ParseText.parseTextToEntries(update_text)

        u_l = Updater(self.step_list,entries).update()
        self.step_list = FormatStructure(u_l).format()
    
        if not len(self.step_list) == 0:
            self.updateStarts(self.step_list[0].start,0)
        else:
            self.start = Plan.STANDARD_START
            self.end = self.start