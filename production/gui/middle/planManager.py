import sys
import os
sys.path.append(os.path.join("./production/logic"))

from plan import Plan
from template import Template
from entry import Entry

class PlanManager():

    def __init__(self,*activationFunctions):
        self.plan = Plan("Heute")
        self.template = Template("Template Theme")
        self.active = self.plan
        self.funcs = activationFunctions

    def splitTemplate(self,template_index,split_index):
        self.active.splitTemplate(template_index,split_index) # must be plan
        self.communicate()

    def atOrSet(self,eOT:Entry):
        if isinstance(self.active,Plan):
            return self.add(eOT)
        else:
            return self.setTemplate(eOT)

    def removeElement(self,index):
        self.active.remove(index)
        self.communicate()
    

    def add(self,eOT):
        eOT = self.active.add(eOT)
        self.communicate()
        return eOT

    def swapActive(self):
        if self.active == self.plan:
            self.active = self.template
        else:
            self.active = self.plan
        self.communicate()
    
    def communicate(self):
        [f() for  f in self.funcs]

    def setPlan(self,plan):
        self.plan = plan
        self.active = plan
        self.communicate()
    
    def setTemplate(self,template):
        self.template = template
        self.active = template
        self.communicate()