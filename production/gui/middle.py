import kivy
kivy.require('1.11.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.recycleview import RecycleView
from kivy.uix.textinput import TextInput

import sys
sys.path.append(".\\production")
from plan import Plan
from template import Template
from entry import Entry


class RV_Templates(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.templates = []

    def addTemplate(self,template:Template):
        index = str(len(self.data))
        self.data.append({"text":index+" "+ template.theme+" "+template.duration})
        self.templates.append(template)


class PlanWidget(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.plan = Plan("Heute")

    def addTemplate(self,template:Template):
        temp = self.plan.add(template)
        self.text = self.plan.getText()
        if not self.structure_List == None:
            self.structure_List.addEntry(temp,self)
        return temp

    def removeElement(self,index):
        self.plan.remove(index)
        self.text = self.plan.getText()

class RV_Structure(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def addEntry(self,eOT:Entry,planW:PlanWidget):
        index = len(self.data)
        self.data.append({"text":str(index)+" "+eOT.toString(),
        "on_press": self.getRemoveEntry(index,planW)
        })
    
    def getRemoveEntry(self,index,planW:PlanWidget):
        def removeEntry():
            self.data.pop(index)
            planW.removeElement(index)
            self.updateStructureLabels(index,planW)
        return removeEntry

    def updateStructureLabels(self,index,planW:PlanWidget):
        i = index
        for e in self.data[index:]:
            e['text'] = str(i) + " " +planW.plan.the_list[i].toString()
            e["on_press"] = self.getRemoveEntry(i,planW)
            i+=1



class MiddleApp(App):

    def build(self):
        pass

