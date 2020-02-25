import sys
import os

from logic.plan import Plan
from logic.routine import Routine
from logic.entry import Entry

class PlanManager():

    def __init__(self,*activationFunctions):
        self.plan = Plan("Heute")
        self.routine = Routine("Routine Theme")
        self.active = self.plan
        self.funcs = list(activationFunctions)
        self.updateStructure =None

    def splitRoutine(self,routine_index,split_index):
        self.active.splitRoutine(routine_index,split_index) # must be plan
        self.communicate()

    def atOrSet(self,eOT:Entry):
        if isinstance(self.active,Plan):
            return self.add(eOT)
        else:
            return self.setRoutine(eOT)

    def removeElement(self,index):
        self.active.remove(index)
        self.communicate()
    
    def rename(self,temp_index,name):
        self.active.step_list[temp_index].theme = name
        self.communicate()

    def add(self,eOT):
        eOT = self.active.add(eOT)
        self.communicate()
        return eOT

    def update(self,theme,text):
        self.active.theme = theme
        self.active.update(text)
        if not self.updateStructure == None:
            self.updateStructure()
    
    def updateText(self,text):
        self.update(self.active.theme,text)

    def updateTheme(self,theme):
        self.active.theme = theme

    def swapActive(self):
        if self.active == self.plan:
            self.active = self.routine
        else:
            self.active = self.plan
        self.communicate()

    def addUpdateStructure(self,updateStructure):
        self.updateStructure = updateStructure
    
    def addCommunication(self, func):
        self.funcs.append(func) 

    def communicate(self):
        [f() for  f in self.funcs]

    def setPlan(self,plan):
        self.plan = plan
        self.active = plan
        self.communicate()
    
    def setRoutine(self,routine):
        self.routine = routine
        self.active = routine
        self.communicate()

    def getTheme(self):
        return self.active.theme