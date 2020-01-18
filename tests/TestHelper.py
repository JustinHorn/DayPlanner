import unittest
import sys
sys.path.append('.\\production\\logic')
import calcTime 
import load 
from entry import Entry 
from plan import Plan 
from template import Template


def createPlan(self,string:str):
    plan = Plan("today")
    ele = None
    currentCharIsLast = lambda i,s: i+1 == len(s)
    addStandardEntry = lambda : plan.add(Entry("00:05","standard"))
    addTemp = lambda:plan.add(self.template)

    for i,e in enumerate(string):
        if e == 'E':
            if not currentCharIsLast(i,string):
                n_char = string[i+1]
                if n_char.isdigit():
                    c = int(n_char)
                    for i in range(c):
                        addStandardEntry()
                elif  n_char == 'S':
                    ele = Entry("00:06","besonders")
                    plan.add(ele)
                else:        
                    addStandardEntry()
            else:        
                addStandardEntry()
        elif e=="T":
            if not currentCharIsLast(i,string):
                if string[i+1].isdigit():
                    c = int(string[+1])
                    for i in range(c):
                        addTemp()
                else:
                    addTemp()
            else:
                addTemp()
    return plan,ele

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
