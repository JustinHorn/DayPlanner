import kivy
kivy.require('1.11.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.recycleview import RecycleView
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty


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


class PlanStructureWidget(FloatLayout):
    plan_t = ObjectProperty()
    structure = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.plan = Plan("Heute")

    def addTemplate(self,template:Template):
        temp = self.plan.add(template)
        self.plan_t.text = self.plan.getText()
        index = len(self.structure.data)
        self.structure.data.append({"text":str(index)+" "+template.toString(),
        "on_press": self.getRemoveEntry(index)
        })
        return temp

    def getRemoveEntry(self,index):
        def removeEntry():
            self.structure.data.pop(index)
            self.removeElement(index)
            self.updateStructureLabels(index)
        return removeEntry

    def updateStructureLabels(self,index):
        i = index
        for e in self.structure.data[index:]:
            e['text'] = str(i) + " " +self.plan.the_list[i].toString()
            e["on_press"] = self.getRemoveEntry(i)
            i+=1

    def removeElement(self,index):
        self.plan.remove(index)
        self.plan_t.text = self.plan.getText()



class MiddleApp(App):

    def build(self):
        pass

