import unittest
import sys
import os 
sys.path.append(os.path.join('./production/logic'))
import Load 
from entry import Entry 
from plan import Plan 
from template import Template



def createPlan(self,string:str):
    plan = Plan("today")
    special_element = None

    for i,e in enumerate(string):
        if e == 'E':
            ele = addToPlan(self,plan,i,string,Entry)
            if not ele == None:
                special_element = ele
        elif e=="T":
            addToPlan(self,plan,i,string,Template)
    return plan,special_element

def addToPlan(self,plan,index,string,classType):
    element = []
    if not len(string) == index+1:
        n_char = string[index+1]
        if n_char.isdigit():
            c = int(n_char)
            for i in range(c):
                addTypeToPlan(self,plan,classType)
        elif  n_char == 'S' and classType == Entry:
            ele = Entry("00:06","besonders")
            plan.add(ele)
            return ele
        else:        
            addTypeToPlan(self,plan,classType)
    else:        
        addTypeToPlan(self,plan,classType)

def addTypeToPlan(self,plan,classType):
    if classType is Template:
        plan.add(self.template)
    else:
        plan.add(Entry("00:05","standard"))

def test_listByInstance(self,step_list,instances:str):
    if instances[0].isdigit():
        self.assertEqual(len(step_list),int(instances[0]))
        instances = instances[1:]

    for i,e in enumerate(instances):
        if e == 'E':
            self.assertEqual(step_list[i].__class__,Entry)
        elif e=="T":
            self.assertEqual(step_list[i].__class__,Template)
        else:
            pass
